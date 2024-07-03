x = ['lucas','baba','meimei']

for i in x:
    print(i)


    def matrix_to_latex(matrix, precision=5, pretext=""):
        """Latex representation of a complex numpy array (with dimension 2)

            Args:
                matrix (ndarray): The matrix to be converted to latex, must have dimension 2.
                precision: (int) For numbers not close to integers, the number of decimal places to round to.
                pretext: (str) Latex string to be prepended to the latex, intended for labels.

            Returns:
                str: Latex representation of the matrix
        """
        out_string = "$$\n{}".format(pretext)
        out_string += "\\begin{bmatrix}\n"
        for row in matrix:
            for amplitude in row:
                num_string = num_to_latex(amplitude, precision=precision)
                out_string += num_string + " & "
            out_string = out_string[:-2]  # remove trailing ampersands
            out_string += " \\\\\n"
        out_string += "\end{bmatrix}\n$$\n"
        return out_string


"""Latex representation of a complex numpy array (with dimension 1 or 2)

                Args:
                    matrix (ndarray): The array to be converted to latex, must have dimension 1 or 2.
                    precision: (int) For numbers not close to integers, the number of decimal places to round to.
                    pretext: (str) Latex string to be prepended to the latex, intended for labels.
                    display_output: (bool) if True, uses IPython.display to display output, otherwise returns the latex string.

                Returns:
                    str: Latex representation of the array, wrapped in $$

                Raises:
                    ValueError: If array can not be interpreted as a numerical numpy array
                    ValueError: If the dimension of array is not 1 or 2
"""
    def array_to_latex(array, precision=5, pretext="", display_output=True):

        try:
            array = np.asarray(array)
            array + 1  # Test array contains numerical data
        except:
            raise ValueError(
                "array_to_latex can only convert numpy arrays containing numerical data, or types that can be converted to such arrays")
        if array.ndim == 1:
            output = vector_to_latex(array, precision=precision, pretext=pretext)
        elif array.ndim == 2:
            output = matrix_to_latex(array, precision=precision, pretext=pretext)
        else:
            raise ValueError("array_to_latex can only convert numpy ndarrays of dimension 1 or 2")
        if display_output:
            display(Math(output))
        else:
            return (output)