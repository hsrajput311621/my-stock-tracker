"""Central configuration for the ETF tracker — Hitesh's portfolio.
Edit PORTFOLIO to change holdings. `yf` is the Yahoo Finance symbol
(NSE tickers use the .NS suffix). If a symbol shows ❓ in the dashboard
health check, fix it here — check the Yahoo Finance quote page for the
correct ticker.
"""

import os

# ---------------------------------------------------------------------------
# Portfolio (key = your Google Sheet / broker ticker)
# "alloc" = % of your total stock book by current value (informational)
# "freq"  = how often you want dip-checks to actually alert on this one
#           (Daily for concentrated/volatile positions, Weekly for smaller)
# ---------------------------------------------------------------------------
PORTFOLIO = {
    # --- SBICAP: largest positions, check daily ---
    "TATAPOWER":  {"name": "Tata Power Company Ltd",       "yf": "TATAPOWER.NS",  "alloc": 15.2, "freq": "Daily"},
    "M&M":        {"name": "Mahindra & Mahindra Ltd",      "yf": "M&M.NS",        "alloc": 15.0, "freq": "Daily"},
    "ICICIBANK":  {"name": "ICICI Bank Ltd",               "yf": "ICICIBANK.NS",  "alloc": 10.7, "freq": "Daily"},
    "TATASTEEL":  {"name": "Tata Steel Ltd",               "yf": "TATASTEEL.NS",  "alloc": 7.2,  "freq": "Daily"},
    "EICHERMOT":  {"name": "Eicher Motors Ltd",             "yf": "EICHERMOT.NS", "alloc": 5.8,  "freq": "Daily"},
    "TATAELXSI":  {"name": "Tata Elxsi Ltd",               "yf": "TATAELXSI.NS", "alloc": 4.1,  "freq": "Daily"},
    "HDFCBANK":   {"name": "HDFC Bank Ltd",                "yf": "HDFCBANK.NS",  "alloc": 3.8,  "freq": "Daily"},
    "TMCV":       {"name": "Tata Motors Ltd (Commercial)", "yf": "TMCV.NS",      "alloc": 2.7,  "freq": "Weekly"},
    "TMPV":       {"name": "Tata Motors Passenger Veh.",   "yf": "TMPV.NS",      "alloc": 2.2,  "freq": "Weekly"},
    "AXISBANK":   {"name": "Axis Bank Ltd",                "yf": "AXISBANK.NS",  "alloc": 2.4,  "freq": "Weekly"},
    "DEEPAKNTR":  {"name": "Deepak Nitrite Ltd",           "yf": "DEEPAKNTR.NS", "alloc": 1.6,  "freq": "Weekly"},
    "INFY":       {"name": "Infosys Ltd",                  "yf": "INFY.NS",      "alloc": 1.4,  "freq": "Daily"},
    "PSUBNKBEES_S": {"name": "Nippon PSU Bank BeES (SBICAP)", "yf": "PSUBNKBEES.NS", "alloc": 1.0, "freq": "Weekly"},

    # --- Upstox ---
    "PNB":        {"name": "Punjab National Bank",         "yf": "PNB.NS",       "alloc": 2.7,  "freq": "Weekly"},
    "MON100_U":   {"name": "Motilal NASDAQ100 ETF (Upstox)","yf": "MON100.NS",   "alloc": 1.8,  "freq": "Daily"},
    "UNIONBANK":  {"name": "Union Bank of India",           "yf": "UNIONBANK.NS","alloc": 1.5,  "freq": "Weekly"},
    "BANKBARODA": {"name": "Bank of Baroda",                "yf": "BANKBARODA.NS","alloc": 1.5,  "freq": "Weekly"},
    "APLAPOLLO":  {"name": "APL Apollo Tubes Ltd",          "yf": "APLAPOLLO.NS","alloc": 1.7,  "freq": "Weekly"},
    "TITAN":      {"name": "Titan Company Ltd",             "yf": "TITAN.NS",    "alloc": 1.3,  "freq": "Weekly"},
    "NIFTYBEES":  {"name": "Nifty 50 BeES",                 "yf": "NIFTYBEES.NS","alloc": 1.1,  "freq": "Daily"},
    "BANKINDIA":  {"name": "Bank of India",                 "yf": "BANKINDIA.NS","alloc": 1.1,  "freq": "Weekly"},
    "NESTLEIND":  {"name": "Nestle India Ltd",               "yf": "NESTLEIND.NS","alloc": 0.8,  "freq": "Weekly"},
    "CDSL":       {"name": "CDSL",                          "yf": "CDSL.NS",     "alloc": 0.9,  "freq": "Weekly"},
    "TCS":        {"name": "TCS",                           "yf": "TCS.NS",      "alloc": 0.4,  "freq": "Daily"},
    "PIDILITIND": {"name": "Pidilite Industries Ltd",       "yf": "PIDILITIND.NS","alloc": 0.3,  "freq": "Weekly"},
    "GOLDBEES":   {"name": "Gold Bees",                     "yf": "GOLDBEES.NS", "alloc": 0.5,  "freq": "Weekly"},
    "DMART":      {"name": "Avenue Supermarts Ltd",         "yf": "DMART.NS",    "alloc": 0.3,  "freq": "Weekly"},
    "IRCTC":      {"name": "IRCTC",                         "yf": "IRCTC.NS",    "alloc": 0.2,  "freq": "Weekly"},
    "ASIANPAINT": {"name": "Asian Paints Ltd",               "yf": "ASIANPAINT.NS","alloc": 0.1, "freq": "Weekly"},

    # --- INDmoney ---
    "MON100_I":   {"name": "Motilal NASDAQ100 ETF (INDmoney)", "yf": "MON100.NS", "alloc": 2.1, "freq": "Daily"},
    "ITIETF":     {"name": "ICICI Prudential IT ETF",       "yf": "ITIETF.NS",   "alloc": 1.9,  "freq": "Daily"},
    "MIDCAPETF":  {"name": "Mirae Nifty Midcap 150 ETF",     "yf": "MIDCAPETF.NS","alloc": 1.6,  "freq": "Weekly"},
    "HDFCSML250": {"name": "HDFC Nifty Smallcap 250 ETF",    "yf": "HDFCSML250.NS","alloc": 1.3, "freq": "Weekly"},
    "PSUBNKBEES_I": {"name": "Nippon PSU Bank BeES (INDmoney)", "yf": "PSUBNKBEES.NS", "alloc": 0.9, "freq": "Weekly"},
    "PHARMABEES": {"name": "Nippon Nifty Pharma ETF",        "yf": "PHARMABEES.NS","alloc": 0.8, "freq": "Weekly"},
    # Yahoo has no UTI Next-50 symbol; NEXT50IETF tracks the same index (proxy for dip %).
    "NEXT50BETA": {"name": "UTI Nifty Next 50 ETF",          "yf": "NEXT50IETF.NS","alloc": 1.0, "freq": "Weekly"},
    "BHARAT22":   {"name": "Bharat 22 ETF",                  "yf": "ICICIB22.NS", "alloc": 0.8,  "freq": "Weekly"},
    "SBIN":       {"name": "State Bank of India",            "yf": "SBIN.NS",     "alloc": 0.4,  "freq": "Weekly"},
    "MOM30IETF":  {"name": "ICICI Nifty200 Momentum30 ETF",  "yf": "MOM30IETF.NS","alloc": 0.05, "freq": "Weekly"},
}
# ---------------------------------------------------------------------------
# ETF watchlist for dip detection (separate from your main PORTFOLIO)
# These are ETFs/funds that we monitor for buying opportunities during dips
# ---------------------------------------------------------------------------
ETFS = {
    "NIFTYBEES":      {"name": "Nifty 50 BeES",               "yf": "NIFTYBEES.NS", "alloc": 1.0, "freq": "Weekly"},
    "BANKBEES":       {"name": "Nifty Bank BeES",             "yf": "BANKBEES.NS", "alloc": 1.0, "freq": "Weekly"},
    "ITBEES":         {"name": "Nifty IT BeES",               "yf": "ITBEES.NS", "alloc": 1.0, "freq": "Weekly"},
    "PHARMABEES":     {"name": "Nifty Pharma BeES",           "yf": "PHARMABEES.NS", "alloc": 1.0, "freq": "Weekly"},
    "NEXT50IETF":     {"name": "Nifty Next 50 ETF",           "yf": "NEXT50IETF.NS", "alloc": 1.0, "freq": "Weekly"},
    "MIDCAPETF":      {"name": "Nifty Midcap 150 ETF",        "yf": "MIDCAPETF.NS", "alloc": 1.0, "freq": "Weekly"},
    "SMALLETF":       {"name": "Nifty Smallcap 100 ETF",      "yf": "SMALLCAPETF.NS", "alloc": 1.0, "freq": "Weekly"},
    "GOLDBEES":       {"name": "Gold BeES",                   "yf": "GOLDBEES.NS", "alloc": 1.0, "freq": "Weekly"},
    "LIQUIDBEES":     {"name": "Liquid BeES",                 "yf": "LIQUIDBEES.NS", "alloc": 1.0, "freq": "Weekly"},
    "PSUBNKBEES":     {"name": "Nifty PSU Bank BeES",         "yf": "PSUBNKBEES.NS", "alloc": 1.0, "freq": "Weekly"},
    "HDFCSML250":     {"name": "HDFC Nifty Smallcap 250 ETF", "yf": "HDFCSML250.NS", "alloc": 1.0, "freq": "Weekly"}
}

# ---------------------------------------------------------------------------
# Notifications (ntfy.sh — free, no account)
# Pick your own random topic name (Setup step 1 in the README) and either
# set it here or as a GitHub Actions secret named NTFY_TOPIC.
# ---------------------------------------------------------------------------
NTFY_TOPIC = os.getenv("NTFY_TOPIC") or "hitesh-stocks-CHANGE-THIS-SUFFIX"
NTFY_SERVER = os.getenv("NTFY_SERVER") or "https://ntfy.sh"

# ---------------------------------------------------------------------------
# Alert thresholds
# ---------------------------------------------------------------------------
DIP_THRESHOLD_PCT = 2.0   # start alerting once a stock is this % below yesterday's close
DIP_STEP_PCT = 1.0        # re-alert on each further 1% step down (anti-spam)

# ---------------------------------------------------------------------------
# Budgets (₹) — informational, shown on the dashboard
# ---------------------------------------------------------------------------
MONTHLY_SIP_BUDGET = 50000
MONTHLY_DIP_BUDGET = 8000

# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------
REFRESH_SECONDS = 60

# Market hours (IST) — Mon-Fri 09:15-15:30
MARKET_OPEN = (9, 15)
MARKET_CLOSE = (15, 30)