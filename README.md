# Stereoscopic Portfolio Optimization

~ Inspired by the work of Lamarcus Coleman

The framework introduces the idea of bottom up optimization via the use of machine learning ensembles applied to certain market microstructure components, along with the top-down approach of the Efficient Frontier model, to create a stereoscopic model.

Ensembles were used consistently with the idea that a porfolio is the composition of 𝑛 market microstructures. The strength of ensembles is that they allow for the aggreagation of multiple, sometimes weak models, to create a more robust model. The usage of ensemble models is heavily emphasised, since their goal is to minimize the cost function. This is analogous to the goal of portfolio optimization, which is to minimize risk.

This strategy implements the traditional Mean-Variance Optimization in combination with Gaussian Mixture Models and Random Forests.
