-- Query to extract Anchor Protocol Daily Deposits and Borrows on Terra Classic
-- Target Environment: Dune Analytics (Terra Classic)

WITH daily_balances AS (
  SELECT
    DATE(block_time) AS date_utc,
    SUM(deposit_amount) / 1e6 AS total_deposits_ust, -- Adjust decimals (UST = 6)
    SUM(borrow_amount) / 1e6 AS total_borrows_ust
  FROM (
      -- Placeholder logic: In Dune V2/DuneSQL, you would query specific decoded tables
      -- e.g. anchor_market_evt_Deposit, anchor_market_evt_Borrow
      -- This is a conceptual query representing the logic required.
      
      -- 1. Deposits (Total aUST supply * Current Exchange Rate)
      -- Simplification: Just summing net flows. 
      -- In reality, query `terra.daily_balances` for the aUST contract address
      -- and multiply by the `exchange_rate` from the `overseer` or `market` contract state.
      
      SELECT
        block_time,
        amount AS deposit_amount,
        0 AS borrow_amount
      FROM anchor_daily_deposits -- conceptual
      
      UNION ALL
      
      SELECT
        block_time,
        0 AS deposit_amount,
        amount AS borrow_amount
      FROM anchor_daily_borrows -- conceptual
  )
  GROUP BY 1
)

SELECT 
    date_utc AS "Date",
    total_deposits_ust AS "Anchor_Deposits",
    total_borrows_ust AS "Anchor_Borrows"
FROM daily_balances
WHERE date_utc >= '2021-01-01' AND date_utc <= '2022-05-30'
ORDER BY 1 ASC;

-- NOTE FOR ANALYST:
-- If using Dune V2 "Terra Classic" dataset:
-- The `anchor_market` contract address is: `terra1sepfj7s0aeg5967uxnfk4thzlerrsktkpelm5s`
-- You may need to query `terra.msgs` where `contract_address` matches and extracting `execute_msg` JSON.
