# The Libra Reserve

**Authors:** Christian Catalini, Oliver Gratry, J. Mark Hou, Sunita Parasuraman, Nils Wernerfelt  
**Revised:** August 14th, 2019

## Abstract

This document contains several parts: (1) What is the purpose of the reserve? (2) How is it getting set up? (3) How do entities interact with it? And (4) How will it change over time?

---

## 1 What Is the Purpose of the Reserve?

Many cryptocurrencies today (e.g., Bitcoin and Ether) have no underlying assets to back them. As a result, speculation and investment have been primary use cases, as with a potential for substantial appreciation many people have acquired these coins hoping to sell them at a higher price later. As beliefs over the longterm value of these currencies and success of their networks fluctuate, so too have their prices, yielding at times massive swings in value.

To drive widespread adoption, Libra is designed to be a currency where any user will know that the value of a Libra today will be close to its value tomorrow and in the future. Just as consumers in Europe know the number of Euros it takes them to buy a coffee today will be similar to the number of Euros it will take them tomorrow, holders of Libra, too, can be confident the value of their coins today will be relatively stable across time.

The reserve is the key mechanism for achieving value preservation. By fully backing each coin with a set of stable and liquid assets (described later) and by working with a competitive group of exchanges and other liquidity providers, users can have confidence that they will be able to sell any Libra coin at or close to the value of the reserve at any time. This gives the coin intrinsic value on day one and helps protect against the speculative swings of other cryptocurrencies. The mechanics of the reserve and the various actors in the system are described later in this section, but, at the outset, it is important to highlight why the reserve was created in the first place — to support stability and value preservation.

## 2 How Is the Reserve Getting Set Up?

There are several parts to this section. First, where is the money for the reserve coming from? Second, how will the reserve be invested? Third, where is it being held? And fourth, what are the actual assets backing each Libra coin?

**Where is the money for the reserve coming from?** The money in the reserve will come from two sources: commitments by members and users of Libra. The association will pay out incentives in Libra coin to Founding Members to encourage adoption by users, merchants, and developers. On the user side, for new Libra coins to be created, there must be an equivalent purchase of Libra for fiat and transfer of that fiat to the reserve. Hence, the reserve will grow as users’ demand for Libra increases. In short, there is only one way to create more Libra — by purchasing more Libra for fiat and growing the reserve.

**How will the reserve be invested?** Users of Libra do not receive a return from the reserve. The reserve will be invested in low-risk assets that will yield interest over time. The revenue from this interest will first go to support the operating expenses of the association — to fund investments in the growth and development of the ecosystem, grants to nonprofit and multilateral organizations, engineering research, etc.

**How is the reserve being held?** The reserve will be held by a geographically distributed network of custodians with investment-grade credit rating to limit counterparty risk. Safeguarding the reserve’s assets, providing high auditability and transparency, avoiding the risks of a centralized reserve, and achieving operational efficiency are the key parameters in custody selection and design.

**What are the actual assets that will be backing each Libra coin?** The actual assets will be a collection of low-volatility assets, including bank deposits and government securities in currencies from stable and reputable central banks. As the value of Libra will be effectively linked to a basket of fiat currencies, from the point of view of any specific currency, there will be fluctuations in the value of Libra. The makeup of the reserve is designed to mitigate the likelihood and severity of these fluctuations, particularly in the negative direction (i.e., even in economic crises). To that end, the above basket has been structured with capital preservation and liquidity in mind. On the capital preservation point, the association will only invest in debt from stable governments with low default probability that are unlikely to experience high inflation. In addition, the reserve has been diversified by selecting multiple governments, rather than just one, to further reduce the potential impact of such events. In terms of liquidity, the association plans to rely on short-dated securities issued by these governments, that are all traded in liquid markets that regularly accommodate daily trading volume in the tens or even hundreds of billions. This allows the size of the reserve to be easily adjusted as the number of Libra in circulation expands or contracts.

### 2.1 How Do Entities Interact With the Reserve?

Users will not directly interface with the reserve. Rather, to support higher efficiency, there will be authorized resellers who will be the only entities authorized by the association to transact large amounts of fiat and Libra in and out of the reserve. These authorized resellers will integrate with exchanges and other institutions that buy and sell cryptocurrencies to users, and will provide these entities with liquidity for users who wish to convert from cash to Libra and back again.

The association does not set monetary policy. It mints and burns coins only in response to demand from authorized resellers. Users do not need to worry about the association introducing inflation into the system or debasing the currency. For new coins to be minted, there must be a commensurate payment of fiat by resellers into the reserve. Through interaction with authorized resellers, the association automatically mints new coins when demand increases and destroys them when the demand contracts. Because the reserve will not be actively managed, any appreciation or depreciation in the value of the Libra will come solely as a result of FX market movements.

The association will encourage the listing of Libra on multiple regulated electronic exchanges throughout the world. These exchanges offer both web portals and mobile apps for users to buy and sell Libra. The association is also discussing ongoing relationships with principal cryptocurrency trading firms and top banking institutions as authorized resellers to allow people the opportunity to exchange their local currencies for Libra as easily as possible.

**Consumer financial protection and law enforcement**

Consumers of financial services and products can be vulnerable. There is a commitment to strong consumer protection in the Libra ecosystem, and the Libra Association recognizes that regulators charged with consumer protection will be keen to engage with those building services to be offered in their jurisdictions. In the early development of the Libra network, its Founding Members are committed to working with authorities to shape a regulatory environment that encourages technological innovation while maintaining high standards of consumer protection.

As with any currency or financial infrastructure, bad actors will try to exploit the Libra network. While the network is open and accessible to everyone with internet access, the network’s main endpoints, in the form of exchanges and wallets, will need to follow applicable laws and regulations and collaborate with law enforcement. In addition, like many other blockchains, the ledger of transactions on the Libra Blockchain will be publicly accessible so that it is possible for third parties to do analysis to detect and penalize fraud.

## 3 How Will the Reserve Change Over Time?

The reserve will remain fully backed across time. This means that today, tomorrow, and in the future, users can have confidence that any Libra coin they hold can be sold for fiat currency at a narrow spread above or below the value of the underlying reserve, when a competitive market for exchanges is present. The association may occasionally change the composition of the basket in response to significant changes in market conditions (e.g., to respond to an economic crisis in one of the represented regions), but the goal will always be value preservation. Further, such a change would require exceptional circumstances and a supermajority vote by the association’s council.

Importantly, the size of the reserve is determined by the size of the balances that users are holding in Libra. Hence, unlike some other cryptocurrencies, supply is not restricted by outside factors. This has the important role of allowing the Libra ecosystem to grow or shrink with demand. It also discourages “runs on the bank” since the typical rationale behind a run is that a coin is only fractionally backed, so users want to get their backing out before others do. With a fully backed coin and a competitive ecosystem of exchanges, it will be possible to convert coins back to fiat at a narrow spread above or below their current value, no matter how many coins are in circulation or how many people have already sold their Libra. The market value of the reserve always supports the value of the fiat currency that users receive if they sell their Libra.

Our goal is for Libra to exist alongside existing currencies. Since Libra will be global, the association decided not to develop its own monetary policy but to inherit the policies of the central banks represented in the basket. As discussed earlier, the mechanics of interfacing with our reserve make our approach very similar to the way in which currency boards (e.g., of Hong Kong) have operated. Whereas central banks can print money at their own discretion, currency boards typically only print local currency when there are sufficient foreign exchange assets to fully back a new minting of notes and coins. Two of the major reasons for implementing such a system are stability — as the underlying assets are selected for their lower volatility — and protection from future abuse (e.g., printing of additional coins in the absence of backing).

A key objective of the project is to provide billions of people with access to a low-volatility cryptocurrency that can serve as a low-friction medium of exchange on an international basis from day one, and can support new digital-native use cases such as micropayments. The Libra Reserve plays a vital role in supporting value preservation, building trust, and protecting the resources users, merchants, and developers bring to the network. Over time, as the network moves to permissionless (see Moving Toward Permissionless Consensus), the association will explore ways to further increase the geographic distribution and resilience of the reserve to economic shocks and to improve how it achieves stability and value preservation for its users.

We look forward to feedback and ideas from researchers and the Libra community as we work together with the association Founding Members toward these goals.

## 4 Acknowledgments

We would like to thank the following people for helpful discussions and feedback on this paper: Adrien Auclert, Ravi Jagadeesan, Scott Duke Kominers, Roberto Rigobon, Catherine Tucker, and Kevin Zhang.
