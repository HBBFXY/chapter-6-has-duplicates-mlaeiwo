def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数: lst - 任意列表
    返回: bool - 如果有重复元素返回 True，否则返回 False
    """
    # 学生实现代码区域
    # 将列表转换为集合，集合会自动去除重复元素
    unique_set = set(lst)
    # 比较原列表和集合的长度，若不相等则有重复元素
    return len(lst) != len(unique_set)

# 主程序 - 测试函数
if __name__ == "__main__":
    # 学生需要提供测试用例
    test_cases = [
        [1, 2, 3],        # 无重复
        [1, 2, 2],        # 有重复
        ["a", "b", "a"],  # 字符串重复
        []                # 空列表
    ]

    # 测试每个用例，编写具体测试代码
    for index, test_case in enumerate(test_cases):
        result = has_duplicates(test_case)
        print(f"测试用例 {index + 1}: {test_case}")
        print(f"是否有重复元素: {result}")
        print("-" * 30)
