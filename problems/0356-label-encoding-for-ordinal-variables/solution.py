def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    order_dict = {word: i for i, word in enumerate(order)}

    encoding = [order_dict[word] if word in order_dict else -1 for word in values]

    return encoding