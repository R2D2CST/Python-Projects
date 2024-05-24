"""
In this module I build my self my own statistical and mathematical models for my wn application uses. This module
includes the following models:
    - general_linear_model.
"""

import matplotlib.pyplot as plt # type: ignore

class general_linear_model ():
    """
    This class recreates a procedure thar for two same size data frames makes a linear regression between
    both of them and returns al their statistical information, also recreates a hypothesis test if the given
    frames are equal or not.
    """

    def __init__ (self, x_independent: list [float], y_dependent: list [float], confidence_level = 0.95, file_path = None):
        self.x_independent = x_independent
        self.y_dependent = y_dependent
        self.confidence_level = confidence_level
        self.file_path = file_path
        (
            self.x_mean,
            self.y_mean,
            self.sx_deviation,
            self.sy_deviation,
            self.r_coefficient,
            self.a_origin,
            self.b_slope,
            self.n_size,
            self.sum_xy,
            self.sum_x_squared,
            self.sum_y_squared
        ) = self.linear_regression ()
        (
            self.p_value,
            self.critical_value,
            self.hypothesis_result
        ) = self.hypothesis_test ()
        pass

    def linear_regression (self) -> tuple:
        """
        Linear regression function f(x)= a + bx
        slope of regression b = r(Sy/Sx)
        origin or intercept a = °Y - b°x
        For the purpose of describing means will be represented as °x or °y
        Args:
            self.x_independent (list [float]): list or numbers integer or float of independent data.
            y_independent (list [float]): list or numbers integer or float of dependent data.
            Important Note x and y list must be of the same size and have ate least 2 or more
            data, otherwise this function will return None preventing an error using this method.
        Returns:
            x_mean (float): mean of the x values.
            y_mean (float): mean of the y values.
            sx_deviation (float): standard deviation of the x values.
            sy_deviation (float): standard deviation of the y values.
            r_coefficient (float): correlation coefficient.
            a_origin (float): origin result of the resolved equation.
            b_slope (float): slope result of the resolved equation.
            n_size (int): population size.
        """
        if len (self.x_independent) == len (self.y_dependent) and len (self.x_independent)>1:
            n_size = len (self.x_independent)
            # mean equation used: x° = sum (xi)/n
            x_mean = sum (self.x_independent)/n_size
            y_mean = sum (self.y_dependent)/n_size
            sx_deviation = (sum ((x - x_mean) ** 2 for x in self.x_independent) / (n_size - 1)) ** 0.5
            sy_deviation = (sum ((y - y_mean) ** 2 for y in self.y_dependent) / (n_size - 1)) ** 0.5
            # Calculate correlation coefficient
            sum_xy = sum (x * y for x, y in zip(self.x_independent, self.y_dependent))
            sum_x_squared = sum (x ** 2 for x in self.x_independent)
            sum_y_squared = sum (y ** 2 for y in self.y_dependent)
            """
            We calculate the Pearson correlation coefficient using the following equation.
                        sum ((x-°x)(y-°y))
            r = ------------------------------------
                ((sum(x-°x)**2)(sum(x-°x)**2))**0.5
            """
            correlation_operation_1 = (n_size * sum_xy - sum (self.x_independent) * sum (self.y_dependent))
            correlation_operation_2 = ((n_size * sum_x_squared - (sum (self.x_independent) ** 2)) * (n_size * sum_y_squared - (sum (self.y_dependent) ** 2))) ** 0.5
            r_coefficient =  correlation_operation_1/correlation_operation_2
            b_slope = r_coefficient * (sy_deviation / sx_deviation)
            a_origin = y_mean - b_slope * x_mean
            return x_mean, y_mean, sx_deviation, sy_deviation, r_coefficient, a_origin, b_slope, n_size, sum_xy, sum_x_squared, sum_y_squared
        else:
            return None

    def hypothesis_test (self) -> tuple:
        """
        Hypothesis test for correlation coefficient.
        H0: The linear regression model with a confidence level is accurate, has a correlation of
            X and Y = 1, so both lists are the same population.
        H1: The linear regression model with a confidence level is not accurate, has a correlation
            of X and Y != 1, so both lists are different populations.
        Args:
            r (float): Correlation coefficient.
            n (int): Number of observations.
        Returns:
            p_value (float): p-value of the hypothesis test.
            critical_value (float): Critical value for the hypothesis test.
            hypothesis_result (str): Result of the hypothesis test.
        """
        # Calculate the critical value of r for a given confidence level
        z_value = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
        if self.confidence_level in z_value:
            critical_value = z_value[self.confidence_level]
        else:
            critical_value = 1.96 / (self.n_size ** 0.5)
        # Calculate p-value
        p_value = 2 * (1 - self.r_coefficient)
        # Perform the hypothesis test
        if p_value < (1 - self.confidence_level):
            hypothesis_result = f"H0: Reject null hypothesis. The model is not accurate at {self.confidence_level * 100}% confidence level."
        else:
            hypothesis_result = f"H1: Accept null hypothesis. The model is accurate at {self.confidence_level * 100}% confidence level."
        return p_value, critical_value, hypothesis_result
    
    def plot_and_save(self):
        """
        Plot the data and save the plot in JPG format if file_path is provided.
        Args:
            file_path (str): File path to save the plot. If None, the plot will not be saved.
        """
        plt.scatter(self.x_independent, self.y_dependent, color='blue')
        plt.xlabel('X Independent')
        plt.ylabel('Y Dependent')
        plt.title('Scatter Plot of X vs Y')
        if self.file_path != None:
            plt.savefig(self.file_path, format='jpg')

    pass

# Last code line.