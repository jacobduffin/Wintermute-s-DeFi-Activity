# Wintermute’s DeFi Activity – Interactive Analytics

This project provides an interactive, data-driven overview of Wintermute’s behaviour across decentralised finance, combining on-chain data analysis with browser-rendered Plotly dashboards. The dashboards are available through GitHub Pages at:

https://jacobduffin.github.io/Wintermute-s-DeFi-Activity/

The site hosts several interactive Plotly figures, including: 

- Token, blockchain, and platform activity clusters

- Transaction frequency and USD volume distributions

- Temporal trends in DeFi activity

- Summaries of on-chain behaviour across major ecosystems

All interactive charts are rendered client-side using Plotly, and no Python execution occurs on the hosted site.

## Full Written Report

A full written analysis accompanies the dashboards:  
**On-Chain Analysis of Wintermute’s DeFi Activity (PDF)**

### Report Summary

The report examines Wintermute’s behaviour across tokens, blockchains, and DeFi platforms by classifying counterparties using DeFiLlama metadata and analysing activity with descriptive statistics, log–log plots, clustering, and minute-level temporal resolution.

**Key findings:**

- **Three-tier token structure:**  
  A small group of core tokens (e.g. SOL, USDT, WBTC) dominate both activity and volume, followed by a broad mid-range of regularly traded assets and a long tail of low-frequency tokens.

- **Chain-specific usage:**  
  Ethereum handles the majority of USD volume, while Solana dominates transaction frequency. Arbitrum also supports significant high-frequency activity.

- **Platform segmentation:**  
  High-activity venues such as Uniswap account for most DeFi interaction, with other platforms playing smaller, secondary roles.

- **Temporal behaviour:**  
  Minute-level data show consistent low-level flow punctuated by sharp high-value spikes, especially on Ethereum and primarily involving major stablecoins such as USDC.

**Overall**, Wintermute operates as a high-volume, multi-chain liquidity provider, distributing activity across networks according to throughput, cost efficiency, and settlement needs.

