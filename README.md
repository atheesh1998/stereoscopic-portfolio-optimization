# Stereoscopic Portfolio Optimization

~ Inspired by the work of Lamarcus Coleman

The framework introduces the idea of portfolio optimization via the use of machine learning ensembles applied to market microstructure components, along with the top-down approach of the Efficient Frontier model, to create a stereoscopic model.

Ensembles are used consistently with the idea that a porfolio is the composition of 𝑛 market microstructures. The strength of ensembles is that they allow for the aggregation of multiple, sometimes weak, models to create more robust ones. The usage of ensemble models is heavily emphasised, since their goal is to minimize the cost function. This is analogous to the goal of portfolio optimization, which is to minimize risk.

This strategy implements the traditional Mean-Variance Optimization in combination with Gaussian Mixture Models and Random Forests. K-Means Clustering is used to identify subgroups within the selected universe.

Equally Weighted -> Efficient Frontier (Top Down) -> Bottom Up Optimization -> Sterescopic Portfolio Optimization

The Bottom Up implementation is built on the equally weighted portfolio except that it, instead of solely weighing the strategies equally, optimized the portfolio by applying the GMM to historical regime detection and used Random Forests to predict which of the historical regimes our current market state fell in.

The SPO Framework builds on the Efficient Frontier Portfolio. Thus, while designing the SPO framework portfolio, the regime predictions are obtained from the Efficient Frontier implementation. A new statistical arbitrage object is then created that takes those regime predictions as a parameter and uses it to create the SPO framework portfolio.
