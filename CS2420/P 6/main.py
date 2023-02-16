from hashmap import HashMap

def main():
    hm = HashMap()
    # with pytest.raises(KeyError):
    #     hm.get((0,0))

    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    # assert hm.get((5,5)) == 6
    # assert hm.get((9,9)) == 10
    hm.set((2,2), 409)
    # assert hm.get((2,2)) == 409




if __name__ == "__main__":
    main()
    