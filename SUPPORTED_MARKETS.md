# 🏦 QUANTEX-BOT — Supported Brokers & Markets

> **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)  
> Every market listed here works across the whole bot: Live Session, Live Signal (Strategy Mode and Scanning Mode), Checkers, Future Signals, Live Payouts, Market Filters and the Live Chart.

---

## ✅ Three Brokers — Fully Supported

QUANTEX-BOT supports **three brokers**. Each one is a full integration with its own live candle feed, payout data and result checking, not just a list of pair names.

| Broker | OTC Markets | Live Markets | Total | Status |
|---|---|---|---|---|
| 🟦 **QUOTEX** | **62** | **28** | **90** | ✅ Fully supported |
| 🟧 **TRADOWIX** | **101** | **15** | **116** | ✅ Fully supported |
| 🟪 **BINOLLA** | **100+** | **—** | **100+** | ✅ Fully supported |

### How broker selection works

- **Pick a broker per feature.** When you open Live Session, Live Signal, a Checker, a Future Signal or AXTIRON FS, the bot asks which broker you trade on.
- **Or set a Primary Broker once.** Go to **Settings → Primary Broker**, choose QUOTEX, TRADOWIX or BINOLLA, and turn on **"Use this broker in all features"**. After that the bot uses your broker automatically everywhere and stops asking.
- **Only markets your broker really offers are shown.** Pair lists, payouts and signals always follow the selected broker, so you never get a signal for a market your broker doesn't have.
- **Closed markets are skipped automatically.** Signal engines never analyse a market whose chart is closed. Scanning Mode and the **Avoid under 80%** filter also skip markets paying less than 80%.

> The bot admin can turn any broker on or off. If a broker is temporarily disabled it disappears from the selection until it is enabled again.

---

## 🟦 QUOTEX

**90 markets in total: 62 OTC + 28 Live**

### OTC Markets — 62
_Forex 41 · Crypto 17 · Commodities 4_

**Forex — 41**

|   |   |   |   |   |
|---|---|---|---|---|
| `AUDCAD_otc` | `AUDCHF_otc` | `AUDJPY_otc` | `AUDNZD_otc` | `AUDUSD_otc` |
| `BRLUSD_otc` | `CADCHF_otc` | `CADJPY_otc` | `CHFJPY_otc` | `EURAUD_otc` |
| `EURCAD_otc` | `EURCHF_otc` | `EURGBP_otc` | `EURJPY_otc` | `EURNZD_otc` |
| `EURUSD_otc` | `GBPAUD_otc` | `GBPCAD_otc` | `GBPCHF_otc` | `GBPJPY_otc` |
| `GBPNZD_otc` | `GBPUSD_otc` | `NZDCAD_otc` | `NZDCHF_otc` | `NZDJPY_otc` |
| `NZDUSD_otc` | `USDARS_otc` | `USDBDT_otc` | `USDCAD_otc` | `USDCHF_otc` |
| `USDCOP_otc` | `USDDZD_otc` | `USDEGP_otc` | `USDIDR_otc` | `USDINR_otc` |
| `USDJPY_otc` | `USDMXN_otc` | `USDNGN_otc` | `USDPHP_otc` | `USDPKR_otc` |
| `USDZAR_otc` |  |  |  |  |

**Crypto — 17**

|   |   |   |   |   |
|---|---|---|---|---|
| `ATOUSD_otc` | `AVAUSD_otc` | `AXSUSD_otc` | `BCHUSD_otc` | `BNBUSD_otc` |
| `BTCUSD_otc` | `DASUSD_otc` | `DOTUSD_otc` | `ETCUSD_otc` | `ETHUSD_otc` |
| `LINUSD_otc` | `LTCUSD_otc` | `SOLUSD_otc` | `TONUSD_otc` | `TRUUSD_otc` |
| `XRPUSD_otc` | `ZECUSD_otc` |  |  |  |

**Commodities — 4**

|   |   |   |   |   |
|---|---|---|---|---|
| `UKBrent_otc` (UK Brent Oil) | `USCrude_otc` (US Crude Oil) | `XAGUSD_otc` (Silver) | `XAUUSD_otc` (Gold) |  |

### Live Markets — 28
_Forex 20 · Commodities 1 · Indices 7_

**Forex — 20**

|   |   |   |   |   |
|---|---|---|---|---|
| `AUDCAD` | `AUDCHF` | `AUDJPY` | `AUDUSD` | `CADJPY` |
| `CHFJPY` | `EURAUD` | `EURCAD` | `EURCHF` | `EURGBP` |
| `EURJPY` | `EURUSD` | `GBPAUD` | `GBPCAD` | `GBPCHF` |
| `GBPJPY` | `GBPUSD` | `USDCAD` | `USDCHF` | `USDJPY` |

**Commodities — 1**

|   |   |   |   |   |
|---|---|---|---|---|
| `XAUUSD` (Gold) |  |  |  |  |

**Indices — 7**

|   |   |   |   |   |
|---|---|---|---|---|
| `AXJAUD` (Australia 200) | `F40EUR` (France 40) | `FTSGBP` (UK 100 (FTSE)) | `HSIHKD` (Hong Kong 50) | `IBXEUR` (Spain 35) |
| `JPXJPY` (Japan 225) | `STXEUR` (Euro Stoxx 50) |  |  |  |

> ✅ **QUOTEX summary:** 62 OTC markets and 28 Live markets are supported, **90 in total**.

---

## 🟧 TRADOWIX

**116 markets in total: 101 OTC + 15 Live**

### OTC Markets — 101
_Forex 43 · Crypto 26 · Commodities 7 · Stocks 25_

**Forex — 43**

|   |   |   |   |   |
|---|---|---|---|---|
| `AUDCAD_otc` | `AUDCHF_otc` | `AUDJPY_otc` | `AUDNZD_otc` | `AUDUSD_otc` |
| `CADCHF_otc` | `CADJPY_otc` | `CHFJPY_otc` | `EURAUD_otc` | `EURCAD_otc` |
| `EURCHF_otc` | `EURGBP_otc` | `EURJPY_otc` | `EURNZD_otc` | `EURSGD_otc` |
| `EURUSD_otc` | `GBPAUD_otc` | `GBPCAD_otc` | `GBPCHF_otc` | `GBPJPY_otc` |
| `GBPNZD_otc` | `GBPUSD_otc` | `NZDCAD_otc` | `NZDCHF_otc` | `NZDJPY_otc` |
| `NZDUSD_otc` | `USDARS_otc` | `USDBDT_otc` | `USDBRL_otc` | `USDCAD_otc` |
| `USDCHF_otc` | `USDCOP_otc` | `USDDZD_otc` | `USDEGP_otc` | `USDIDR_otc` |
| `USDINR_otc` | `USDJPY_otc` | `USDMXN_otc` | `USDNGN_otc` | `USDPHP_otc` |
| `USDPKR_otc` | `USDTRY_otc` | `USDZAR_otc` |  |  |

**Crypto — 26**

|   |   |   |   |   |
|---|---|---|---|---|
| `APTUSD_otc` | `ARBUSD_otc` | `ATOMUSD_otc` | `AVAXUSD_otc` | `AXSUSD_otc` |
| `BCHUSD_otc` | `BNBUSD_otc` | `BTCUSD_otc` | `DASHUSD_otc` | `DOGEUSD_otc` |
| `DOTUSD_otc` | `ETCUSD_otc` | `ETHUSD_otc` | `GALAUSD_otc` | `LINKUSD_otc` |
| `LTCUSD_otc` | `MANAUSD_otc` | `MELANIAUSD_otc` | `SOLUSD_otc` | `TIAUSD_otc` |
| `TONUSD_otc` | `TRUMPUSD_otc` | `TRXUSD_otc` | `WIFUSD_otc` | `XRPUSD_otc` |
| `ZECUSD_otc` |  |  |  |  |

**Commodities — 7**

|   |   |   |   |   |
|---|---|---|---|---|
| `BCOUSD_otc` (Brent Oil) | `COPPERUSD_otc` (Copper) | `WTIUSD_otc` (WTI Crude Oil) | `XAGUSD_otc` (Silver) | `XAUUSD_otc` (Gold) |
| `XPDUSD_otc` (Palladium) | `XPTUSD_otc` (Platinum) |  |  |  |

**Stocks — 25**

|   |   |   |   |   |
|---|---|---|---|---|
| `AAPL_otc` | `AMD_otc` | `AMZN_otc` | `ANTH_otc` | `AXP_otc` |
| `BA_otc` | `DIS_otc` | `GOOG_otc` | `GS_otc` | `INTC_otc` |
| `JNJ_otc` | `JPM_otc` | `KO_otc` | `MCD_otc` | `META_otc` |
| `MSFT_otc` | `NFLX_otc` | `NKE_otc` | `NVDA_otc` | `OAIA_otc` |
| `PFE_otc` | `TSLA_otc` | `V_otc` | `WMT_otc` | `XOM_otc` |

### Live Markets — 15
_Forex 13 · Crypto 2_

**Forex — 13**

|   |   |   |   |   |
|---|---|---|---|---|
| `AUDJPY` | `AUDUSD` | `EURAUD` | `EURCAD` | `EURCHF` |
| `EURGBP` | `EURJPY` | `EURUSD` | `GBPJPY` | `GBPUSD` |
| `USDCAD` | `USDCHF` | `USDJPY` |  |  |

**Crypto — 2**

|   |   |   |   |   |
|---|---|---|---|---|
| `BTCUSD` | `ETHUSD` |  |  |  |

> ✅ **TRADOWIX summary:** 101 OTC markets and 15 Live markets are supported, **116 in total**.

---

## 🟪 BINOLLA

**100+ markets.** BINOLLA's market list is read directly from the BINOLLA data feed, so every market BINOLLA lists is picked up by the bot automatically, including new ones, with no update needed.

- Live Session, Live Signal (Strategy and Scanning Mode), Checkers, Future Signals, Live Payouts and the Live Chart all work on BINOLLA.
- BINOLLA results are settled from the closed candle as soon as BINOLLA publishes it.

> 📋 The full BINOLLA market list will be added here.

---

## 🕐 OTC vs Live Markets

| | OTC | Live |
|---|---|---|
| **Availability** | 24/7, weekends included | Mon–Fri, during market hours |
| **Price source** | Broker-generated OTC price | Real market price |
| **Best for** | Trading any time | Main trading sessions |
| **Checker** | OTC Checker | Live Checker |
| **Future Signals** | OTC Market FS | Live Market FS |

---

## 📞 Support

- **Telegram**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)
- **Channel**: [@Quantexbot1](https://t.me/Quantexbot1)
- **Community Group**: [t.me/quantexlounge](https://t.me/quantexlounge)
- **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)
