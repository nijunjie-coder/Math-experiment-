"""使用 SymPy 计算 3×3 符号矩阵的行列式并验证已知答案。"""
from sympy import Matrix, pprint, symbols


def main():
    variables = symbols("a b c d e f g h i")
    matrix = Matrix(3, 3, variables)
    determinant = matrix.det()
    print("3×3 符号矩阵：")
    pprint(matrix)
    print("行列式：", determinant)

    # 按第一行展开：1×4 - 2×(-25) + 3×(-20) = -6。
    example = Matrix([[1, 2, 3], [0, 4, 5], [5, 0, 1]])
    result = determinant.subs(dict(zip(variables, list(example))))
    direct_result = example.det()
    expected = -6
    if result != expected or direct_result != expected:
        raise AssertionError(
            f"验证失败：期望 {expected}，代入结果 {result}，直接计算结果 {direct_result}"
        )
    print("\n验证矩阵：")
    pprint(example)
    print(f"符号公式代入：{result}；直接计算：{direct_result}")
    print(f"验证通过：行列式 = {result}（已知答案为 {expected}）")


if __name__ == "__main__":
    main()
