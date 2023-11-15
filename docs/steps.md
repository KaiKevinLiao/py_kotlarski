My steps are based on Li and Vuong (1998) and Krasnokutskaya (2011).

1. Estimate the joint characteristic function of $(Y_1, Y_2)$ by its empirical counterpart.
   $$\hat{\Psi}(t_1, t_2) = \frac{1}{n} \sum_{j=1}^n \exp \left(i t_1 \cdot Y_{1j}+i t_2 \cdot Y_{2j}\right)$$

2. Estimate the derivative of $\hat{\Psi}(t_1, t_2)$ with respect to $t_1$ by
   $$\hat{\Psi}_1(t_1, t_2) = \frac{1}{n} \sum_{j=1}^n i  \cdot Y_{1j}\exp \left(i t_1 \cdot Y_{1j}+i t_2 \cdot Y_{2j}\right)$$

3. Estimate the characteristic functions by
    $$
    \begin{aligned}
    \widehat{\Phi}_{X}(t) & =\exp \left(\int_0^t \frac{\widehat{\Psi}_{1}\left(0, u\right)}{\widehat{\Psi}\left(0, u\right)} d u-i t E\left[X\right]\right), \\
    \widehat{\Phi}_{\varepsilon_1}(t) & =\frac{\widehat{\Psi}(t, 0)}{\widehat{\Phi}_{X}(t)}, \\
    \widehat{\Phi}_{\varepsilon_2}(t) & =\frac{\widehat{\Psi}(0, t)}{\widehat{\Phi}_{X}(t)} .
    \end{aligned}
    $$

4. Transform the characteristic functions to density functions, where $T$ is a smoothing parameter.
    $$\hat{f}\left(u\right)=\frac{1}{2 \pi} \int_{-T}^T \exp \left(-i t u\right) \widehat{\Phi}(t) d t$$