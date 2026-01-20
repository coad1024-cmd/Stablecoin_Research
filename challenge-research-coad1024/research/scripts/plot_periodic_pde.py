
import numpy as np
import matplotlib.pyplot as plt

def solve_periodic_pde():
    # Parameters
    T_days = 100
    T = T_days / 365.0
    r = 0.03
    R = 0.073  # 7.30%
    sigma = 0.9 # Volatility from Table 1 for ETH
    
    Hu_param = 2.0
    Hd_param = 0.25
    
    # Grid parameters
    S_min = 0.4
    S_max = 1.7
    NS = 131 # Number of spatial points
    S = np.linspace(S_min, S_max, NS)
    dS = S[1] - S[0]
    
    # Time stepping
    # Stability condition for explicit scheme: dt <= dS^2 / (sigma^2 * S_max^2)
    # 0.01^2 / (0.81 * 1.7^2) = 1e-4 / 2.34 ~= 4e-5
    NT = 6000
    dt = T / NT
    t_grid = np.linspace(0, T, NT+1)
    
    # Initial guess for W(0, S)
    # A generic guess: W(0, S) = S, or just 1.
    # W_A behaves like a bond, so close to 1.
    W_old_0 = np.ones(NS) 
    
    # Iteration storage
    W_curr = np.zeros((NT+1, NS))
    
    # Barrier functions
    def get_Hu_t(t):
        # Hu(t) = 0.5 * ((1 + R*t) + Hu_param / (1 + R*t) * (1+R*t)? No wait
        # From text logic: VB = 2S - VA. VA = 1 + Rt. VB = 2S - (1+Rt).
        # Trigger VB >= Hu_param. 2S >= Hu_param + 1 + Rt => S >= (Hu_param + 1 + Rt)/2
        return (Hu_param + 1 + R*t) / 2.0

    def get_Hd_t(t):
        # Trigger VB <= Hd_param. 2S <= Hd_param + 1 + Rt => S <= (Hd_param + 1 + Rt)/2
        return (Hd_param + 1 + R*t) / 2.0

    # Iteration loop
    max_iter = 5
    tolerance = 1e-3
    
    for k in range(max_iter):
        print(f"Iteration {k+1}...")
        
        # 1. Set terminal condition at T
        # WA(T, S) = R*T + WA(0, S - RT/2)? 
        # Check Eq 3.5: WA(T, S) = RT + WA(0, S * exp(-RT/2) ???
        # Text Eq 3.5 says: WA(T, S) = RT + WA(0, S - 1/2 * RT) ??
        # Let's re-read line 2037: WA(0, S_T - RT/2) * 1_{...}
        # Line 2185: WA(T, S) = RT + WA(0, S - 1/2 RT).
        # Wait, Eq 3.1 says S_{T} - RT/2.
        # But Eq 3.2 says Pt is GBM. S_t = Pt / (beta P0).
        # If Pt is GBM, S_t is GBM (since beta is constant between resets).
        # However, at T (regular payout), beta jumps.
        # beta_new = beta_old * (2 Pt) / (2 Pt - beta_old P0 RT).
        # This implies S jumps? S = Pt / (beta P0).
        # S_new = Pt / (beta_new P0) = Pt / (beta_old P0 * (2Pt)/(2Pt - beta P0 RT)) 
        #       = S_old * (2Pt - beta P0 RT) / (2Pt)
        #       = S_old * (1 - (beta P0 RT)/(2Pt))
        #       = S_old * (1 - RT / (2 S_old)) = S_old - RT/2.
        # So yes, S jumps to S - RT/2.
        # So WA(T, S) = RT + W_old_0 evaluated at (S - RT/2).
        
        # Interpolate W_old_0 at S - RT/2
        S_mapped = S - R*T/2.0
        # Clamp or handle out of bounds for interpolation?
        # If S - RT/2 < S_min, we need to extrapolate or use boundary.
        # Since we only solve for Hd(T) < S < Hu(T), we only care about those points.
        
        W_T = R*T + np.interp(S_mapped, S, W_old_0)
        
        W_curr[NT, :] = W_T
        
        # 2. Time stepping backward
        for n in range(NT-1, -1, -1):
            t = t_grid[n]
            Hu = get_Hu_t(t)
            Hd = get_Hd_t(t)
            
            # Identify active nodes
            # indices where Hd < S < Hu
            idx = np.where((S > Hd) & (S < Hu))[0]
            
            if len(idx) == 0:
                continue
                
            # Explicit update
            # W(n) = W(n+1) - dt * ( PDE_operator(W(n+1)) )
            # However, we want W_t = -L W. 
            # W(t) - W(t+dt) / (-dt) = L W.
            # W(t) = W(t+dt) - dt * L W(t+dt).
            # L W = rS W_S + 0.5 sigma^2 S^2 W_SS - r W.
            
            # Using central differences for space
            
            w_next = W_curr[n+1, :]
            
            for i in idx:
                s_val = S[i]
                
                # Boundary handling for w_next interpolation
                def get_w(s_query, t_next_val):
                    # Helper to get w at n+1, handling boundaries
                    # If s_query is outside (Hd_next, Hu_next), we must use BCs.
                    # But for explicit scheme, we just use the grid values from previous step.
                    # However, if grid neighbor is outside the domain of *current* step,
                    # strictly it should follow the solution in that region.
                    # The paper defines the PDE only on the domain.
                    # On boundary, BC applies.
                    
                    # Check current boundaries or next boundaries?
                    # The explicit stencil uses values at n+1.
                    # If neighbor is outside [Hd(t), Hu(t)], we should use BC at time t?
                    # Or BC at time t+dt?
                    # Using BC at time t+dt for determining neighbor values seems correct.
                    Hu_next = get_Hu_t(t_next_val)
                    Hd_next = get_Hd_t(t_next_val)
                    
                    if s_query >= Hu_next:
                        # WA(t, Hu) = Rt + WA(0, 1)
                        return R*t_next_val + np.interp(1.0, S, W_old_0)
                    elif s_query <= Hd_next:
                        # WA(t, Hd) = Rt + 1 - Hd + Hd * WA(0, 1)
                        # Note: Hd in formula (3.7) is the parameter Hd or Hd(t)?
                        # Eq 3.7: "1 - Hd + Hd WA(0, 1)". Given Hd(t) formula involves 'Hd',
                        # it's likely the constant parameter Hd (0.25).
                        return R*t_next_val + (1 - Hd_param) + Hd_param * np.interp(1.0, S, W_old_0)
                    else:
                        return np.interp(s_query, S, w_next)

                # Standard standard 3-point stencil
                # But we can just use array indexing if neighbors are inside
                # For safety near boundaries, let's use the helper or direct check
                
                # Left neighbor
                if i > 0:
                    val_minus = w_next[i-1] # Grid point
                    # If S[i-1] is out of bounds (<= Hd(t+dt)), we should technically overwrite it with BC?
                    # Let's simple check:
                    Hu_next = get_Hu_t(t_grid[n+1])
                    Hd_next = get_Hd_t(t_grid[n+1])
                    
                    if S[i-1] <= Hd_next:
                         val_minus = R*t_grid[n+1] + (1 - Hd_param) + Hd_param * np.interp(1.0, S, W_old_0)
                else:
                    # Boundary condition
                     val_minus = R*t_grid[n+1] + (1 - Hd_param) + Hd_param * np.interp(1.0, S, W_old_0)

                # Right neighbor
                if i < NS-1:
                    val_plus = w_next[i+1]
                    Hu_next = get_Hu_t(t_grid[n+1])
                    if S[i+1] >= Hu_next:
                        val_plus = R*t_grid[n+1] + np.interp(1.0, S, W_old_0)
                else:
                    val_plus = R*t_grid[n+1] + np.interp(1.0, S, W_old_0)
                
                val_center = w_next[i]
                
                # Derivatives
                delta_W = val_plus - val_minus
                delta2_W = val_plus - 2*val_center + val_minus
                
                W_s = delta_W / (2*dS)
                W_ss = delta2_W / (dS**2)
                
                L_W = r * s_val * W_s + 0.5 * sigma**2 * s_val**2 * W_ss - r * val_center
                
                # Update
                W_curr[n, i] = val_center - dt * (-L_W) # W_t = - L_W for backward eq?
                # Wait.
                # W(t) approx W(t+dt) - dt * W_t(t+dt)
                # W_t is usually defined as forward derivative?
                # Eq: W_t + LW = 0 => W_t = -LW.
                # W(t) = W(t+dt) - dt * (-LW) = W(t+dt) + dt * LW.
                # Let's check signs.
                # Discounting logic: Price = exp(-r dt) * E[Price_next].
                # E[Price_next] approx Price + dt * (rS W_s + 0.5 sigma^2 S^2 W_ss).
                # So Price(t) approx (1 - r dt) * (Price + dt(...))
                # = Price + dt (rS W_s + 0.5 sigma^2 S^2 W_ss - r Price).
                # Yes, + dt * LW.
                
                W_curr[n, i] = val_center + dt * L_W

            # Fill values outside active region with BCs for current time t
            # (Just for plotting/completeness, though next step only needs interior/boundary values)
            W_curr[n, S >= Hu] = R*t + np.interp(1.0, S, W_old_0)
            W_curr[n, S <= Hd] = R*t + (1 - Hd_param) + Hd_param * np.interp(1.0, S, W_old_0)

        # Check convergence
        diff = np.max(np.abs(W_curr[0, :] - W_old_0))
        print(f"Max diff: {diff}")
        if diff < tolerance:
            print("Converged.")
            break
        
        W_old_0 = W_curr[0, :].copy()

    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot W_A(0, S)
    # Only valid for Hd(0) < S < Hu(0)
    Hd0 = get_Hd_t(0)
    Hu0 = get_Hu_t(0)
    
    mask = (S >= Hd0) & (S <= Hu0)
    plt.plot(S[mask], W_curr[0, mask], label='Class A Price $W_A(0, S)$', color='blue')
    
    # Add bounds
    plt.axvline(Hd0, color='r', linestyle='--', label='Lower Reset Barrier $H_d(0)$')
    plt.axvline(Hu0, color='g', linestyle='--', label='Upper Reset Barrier $H_u(0)$')
    
    plt.title('Class A Coin Price vs Relative ETH Price')
    plt.xlabel('Relative ETH Price $S$')
    plt.ylabel('Price $W_A$')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('stablecoin_pricing.png')
    print("Plot saved to stablecoin_pricing.png")

if __name__ == "__main__":
    solve_periodic_pde()
