def delete_nth(order,max_e):
    for i in order:
        if order.count(i) > max_e:
            order.reverse()
            order.remove(i)
            order.reverse()
            delete_nth(order,max_e)
    return order
        