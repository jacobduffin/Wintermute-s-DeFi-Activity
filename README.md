# Wintermute’s DeFi Activity – Interactive Analytics

This project provides an interactive visual overview of Wintermute’s DeFi activity across tokens, blockchains, and platforms. The dashboards are available through GitHub Pages at:

https://jacobduffin.github.io/Wintermute-s-DeFi-Activity/

The site hosts several interactive Plotly figures, including: 

- Token, blockchain, and platform activity clusters

- Transaction frequency and USD volume distributions

- Temporal trends in DeFi activity

- Summaries of on-chain behaviour across major ecosystems

The temporal activity figure is presented as a static selection rather than a dynamic one.
The original notebook uses an ipywidgets dropdown to switch between tokens, blockchains, and platforms; however, widget controls cannot operate in GitHub Pages, so the exported HTML contains only the selected version of the plot.

All interactive charts are rendered client-side using Plotly, and no Python execution occurs on the hosted site.

