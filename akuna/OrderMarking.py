import json
class OrderMarking(object):
    def __init__(self):
        self._message = {}
        self.markingPosition = {}
        self.order = {}

    def on_event(self,message):
        self._message = json.loads(message)
        type = self._message['type']
        if type == 'NEW':
            if self._message['side'] == 'SELL':
                return self.onSell()
            else:
                return self.onBuy()
        elif type == 'ORDER_ACK':
            return self.onOrderAck()

        elif type == 'ORDER_REJECT':
            return self.onOrderReject()

        elif type == 'CANCEL':
            return self.onCancel()

        elif type == 'CANCEL_ACK':
            return self.onCancelAck()

        elif type == 'CANCEL_REJECT':
            return self.onCancelReject()

        elif type == 'FILL':
            return self.onFill()

    def onSell(self):
        order_id = self._message['order_id']
        quantity, remaining = self._message['quantity'], self._message['quantity']
        symbol = self._message['symbol']
        self.order[order_id] = ("SELL",symbol, quantity, remaining)
        self.markingPosition[symbol] = self.markingPosition.get(symbol,0) - quantity
        return self.markingPosition[symbol]

    def onBuy(self):
        order_id = self._message['order_id']
        quantity,remaining = self._message['quantity'], self._message['quantity']
        symbol = self._message['symbol']
        self.order[order_id] = ("BUY", symbol, quantity, remaining)
        self.markingPosition[symbol] = self.markingPosition.get(symbol,0)
        return self.markingPosition[symbol]

    def onOrderAck(self):
        order_id = self._message['order_id']
        if order_id not in self.order:
            return 0
        symbol = self.order[order_id][1]
        return self.markingPosition[symbol]

    def onOrderReject(self):
        order_id = self._message['order_id']
        if order_id not in self.order:
            return 0
        side, symbol, quantity, remaining = self.order[order_id]
        if side == "SELL":
            self.markingPosition[symbol] += quantity
        self.order.pop(order_id)
        return self.markingPosition[symbol]

    def onCancel(self):
        order_id = self._message['order_id']
        if order_id not in self.order:
            return 0
        symbol = self.order[order_id][1]
        print(self.order)
        print(self.markingPosition)
        return self.markingPosition[symbol]

    def onCancelAck(self):
        order_id = self._message['order_id']
        if order_id not in self.order:
            return 0
        side, symbol, quantity, remaining = self.order[order_id]
        print(" ")
        print(self.order)
        print(self.markingPosition)
        if side == "SELL":
            self.markingPosition[symbol] += remaining
        return self.markingPosition[symbol]

    def onCancelReject(self):
        order_id = self._message['order_id']
        if order_id not in self.order:
            return 0
        else:
            symbol = self.order[order_id][1]
        return self.markingPosition[symbol]

    def onFill(self):
        order_id = self._message['order_id']
        if order_id not in self.order:
            return 0
        side, symbol, quantity, remaining = self.order[order_id]
        filled_quantity = self._message['filled_quantity']
        remaining -= filled_quantity
        self.order[order_id] = (side,symbol,quantity,remaining)
        if side == "BUY":
            self.markingPosition[symbol] = self.markingPosition.get(symbol,0) + filled_quantity
        return self.markingPosition[symbol]


def assertEqual(a, b):
    if a != b:
        print(False)
    else:
        print(True)

if __name__ == '__main__':
    print("###### test 1 ########")
    M = OrderMarking()
    str = json.dumps({"type": "NEW", "symbol": "IMIMP", "order_id": 1, "side": "SELL", "quantity": 800,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str)) #-800 0
    assertEqual(M.on_event(str), -800)

    str = json.dumps(
        {"type": "ORDER_REJECT", "order_id": 1, "reason": "SYMBOL_UNKNOWN", "time": "2017-03-15T10:15:10.975332"})
    # print(M.on_event(str)) #0 2
    assertEqual(M.on_event(str), 0)  # 2

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 2, "side": "BUY", "quantity": 2000,
                      "time": "2017-03-15T10:15:10.975492"})
    # print(M.on_event(str)) #0 3
    assertEqual(M.on_event(str), 0)  # 3

    str = json.dumps({"type": "ORDER_ACK", "order_id": 2, "time": "2017-03-15T10:15:10.975606"})
    # print(M.on_event(str)) #0 4
    assertEqual(M.on_event(str), 0)  # 4

    str = json.dumps({"type": "FILL", "order_id": 2, "filled_quantity": 2000, "remaining_quantity": 0,
                      "time": "2017-03-15T10:15:10.975717"})
    # print(M.on_event(str)) #2000 5
    assertEqual(M.on_event(str), 2000)  # 5

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 3, "side": "SELL", "quantity": 700,
                      "time": "2017-03-15T10:15:10.975860"})
    # print(M.on_event(str)) #1300 6
    assertEqual(M.on_event(str), 1300)  # 6

    str = json.dumps({"type": "ORDER_ACK", "order_id": 3, "time": "2017-03-15T10:15:10.975966"})
    # print(M.on_event(str)) #1300  7
    assertEqual(M.on_event(str), 1300)  # 7

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 4, "side": "SELL", "quantity": 1500,
                      "time": "2017-03-15T10:15:10.976067"})
    # print(M.on_event(str)) #-200  8
    assertEqual(M.on_event(str), -200)  # 8

    str = json.dumps({"type": "ORDER_ACK", "order_id": 4, "time": "2017-03-15T10:15:10.976170"})
    #print(M.on_event(str)) #-200  9
    assertEqual(M.on_event(str), -200)  # 9

    str = json.dumps({"type": "CANCEL", "order_id": 3, "time": "2017-03-15T10:15:10.976431"})
    # print(M.on_event(str)) #-200  10
    assertEqual(M.on_event(str), -200)  # 10

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 5, "side": "SELL", "quantity": 900,
                      "time": "2017-03-15T10:15:10.976536"})
    # print(M.on_event(str)) #-1100  11
    assertEqual(M.on_event(str), -1100)  # 11

    str = json.dumps({"type": "CANCEL_ACK", "order_id": 3, "time": "2017-03-15T10:15:10.976653"})
    # print(M.on_event(str)) #-400 12
    assertEqual(M.on_event(str), -400)  # 12

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 6, "side": "SELL", "quantity": 800,
                      "time": "2017-03-15T10:15:10.976778"})
    # print(M.on_event(str)) #-1200 13
    assertEqual(M.on_event(str), -1200)  # 13

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 7, "side": "BUY", "quantity": 1700,
                      "time": "2017-03-15T10:15:10.976893"})
    # print(M.on_event(str)) #-1200 14
    assertEqual(M.on_event(str), -1200)  # 14

    str = json.dumps({"type": "ORDER_ACK", "order_id": 5, "time": "2017-03-15T10:15:10.977002"})
    # print(M.on_event(str)) #-1200 15
    assertEqual(M.on_event(str), -1200)  # 15

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 8, "side": "SELL", "quantity": 1300,
                      "time": "2017-03-15T10:15:10.977103"})
    # print(M.on_event(str)) #-2500 16
    assertEqual(M.on_event(str), -2500)  # 16

    str = json.dumps({"type": "ORDER_ACK", "order_id": 6, "time": "2017-03-15T10:15:10.977206"})
    # print(M.on_event(str)) #-2500 17
    assertEqual(M.on_event(str), -2500)  # 17

    str = json.dumps({"type": "CANCEL", "order_id": 7, "time": "2017-03-15T10:15:10.977295"})
    # print(M.on_event(str)) #-2500 18
    assertEqual(M.on_event(str), -2500)  # 18

    str = json.dumps({"type": "ORDER_REJECT", "order_id": 7, "reason": "FIRM_RISK_LIMIT_EXCEEDED",
                      "time": "2017-03-15T10:15:10.977395"})
    # print(M.on_event(str)) #-2500 19
    assertEqual(M.on_event(str), -2500)  # 19

    str = json.dumps({"type": "CANCEL", "order_id": 6, "time": "2017-03-15T10:15:10.977515"})
    # print(M.on_event(str)) #-2500 20
    assertEqual(M.on_event(str), -2500)  # 20

    str = json.dumps({"type": "ORDER_REJECT", "order_id": 8, "reason": "FIRM_RISK_LIMIT_EXCEEDED",
                      "time": "2017-03-15T10:15:10.977665"})
    # print(M.on_event(str)) #-1200 21
    assertEqual(M.on_event(str), -1200)  # 21
    # my additional cases

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 9, "side": "BUY", "quantity": 1000,
                      "time": "2017-03-15T11:15:10.977103"})
    assertEqual(M.on_event(str), -1200)  # 22

    str = json.dumps({"type": "ORDER_ACK", "order_id": 9, "time": "2017-03-15T11:15:10.977206"})
    assertEqual(M.on_event(str), -1200)  # 23

    str = json.dumps({"type": "FILL", "order_id": 9, "filled_quantity": 200, "remaining_quantity": 700,
                      "time": "2017-03-15T11:15:10.975717"})
    assertEqual(M.on_event(str), -1000)  # 24

    str = json.dumps({"type": "FILL", "order_id": 9, "filled_quantity": 1000, "remaining_quantity": 0,
                      "time": "2017-03-15T11:15:10.975717"})
    assertEqual(M.on_event(str), 0)  # 25
    """
    print("###### test 2 ########")
    M = OrderMarking()
    str = json.dumps({"type": "NEW", "symbol": "IMIMP", "order_id": 1, "side": "BUY", "quantity": 800,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str)) #1 0
    assertEqual(M.on_event(str), 0)

    str = json.dumps({"type": "FILL", "order_id": 1, "filled_quantity": 500, "remaining_quantity": 300,
                      "time": "2017-03-15T11:15:10.975717"})
    # print(M.on_event(str)) #2 500
    assertEqual(M.on_event(str), 500)


    str = json.dumps({"type": "CANCEL", "order_id": 1, "time": "2017-03-15T10:15:10.976431"})
    # print(M.on_event(str)) #500  10
    assertEqual(M.on_event(str), 500)  # 10

    str = json.dumps({"type": "CANCEL_ACK", "order_id": 1, "time": "2017-03-15T10:15:10.976653"})
    print(M.on_event(str))
    assertEqual(M.on_event(str), 500)  # 12
    """
    print("###### test 3 ########")
    str = json.dumps({"type": "NEW", "symbol": "IMIMP", "order_id": 1, "side": "SELL", "quantity": 900,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str)) #1 0
    assertEqual(M.on_event(str), -900)

    str = json.dumps({"type": "ORDER_ACK", "order_id": 1, "time": "2017-03-15T10:15:10.975606"})
    # print(M.on_event(str)) #0 4
    assertEqual(M.on_event(str), -900)  # 4

    str = json.dumps({"type": "CANCEL", "order_id": 1, "time": "2017-03-15T10:15:10.976431"})
    # print(M.on_event(str)) #500  10
    assertEqual(M.on_event(str), -900)  # 10

    str = json.dumps({"type": "CANCEL_ACK", "order_id": 1, "time": "2017-03-15T10:15:10.976653"})
    print(M.on_event(str))
    assertEqual(M.on_event(str), 0)  # 12

    str = json.dumps({"type": "NEW", "symbol": "AAPL", "order_id": 2, "side": "BUY", "quantity": 400,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str)) #1 0
    assertEqual(M.on_event(str), 0)

    str = json.dumps(
        {"type": "ORDER_REJECT", "order_id": 2, "reason": "SYMBOL_UNKNOWN", "time": "2017-03-15T10:15:10.975332"})
    # print(M.on_event(str)) #0 2
    assertEqual(M.on_event(str), 0)  # 2

    str = json.dumps({"type": "NEW", "symbol": "AAPL", "order_id": 3, "side": "BUY", "quantity": 1800,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str)) #1 0
    assertEqual(M.on_event(str), 0)

    str = json.dumps({"type": "CANCEL_ACK", "order_id": 3, "time": "2017-03-15T10:15:10.976653"})
    # print(M.on_event(str))
    assertEqual(M.on_event(str), 0)  # 12

    str = json.dumps({"type": "FILL", "order_id": 3, "filled_quantity": 2000, "remaining_quantity": 0,
                      "time": "2017-03-15T10:15:10.975717"})
    # print(M.on_event(str)) #2000 5
    assertEqual(M.on_event(str), 1800)  # 5

    str = json.dumps({"type": "NEW", "symbol": "IMIMP", "order_id": 4, "side": "SELL", "quantity": 800,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str)) #-800 0
    assertEqual(M.on_event(str), 1100)

    str = json.dumps(
        {"type": "ORDER_REJECT", "order_id": 4, "reason": "SYMBOL_UNKNOWN", "time": "2017-03-15T10:15:10.975332"})
    # print(M.on_event(str)) #0 2
    assertEqual(M.on_event(str), 1800)

    str = json.dumps({"type": "CANCEL", "order_id": 3, "time": "2017-03-15T10:15:10.976431"})
    # print(M.on_event(str)) #500  10
    assertEqual(M.on_event(str), 1800)  # 10

    str = json.dumps({"type": "CANCEL_REJECT", "order_id": 3, "time": "2017-03-15T10:15:10.976431"})
    # print(M.on_event(str)) #500  10
    assertEqual(M.on_event(str), 1800)  # 10

    str = json.dumps({"type": "NEW", "symbol": "IMIMP", "order_id": 5, "side": "SELL", "quantity": 900,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str)) #1 0
    assertEqual(M.on_event(str), -900)










