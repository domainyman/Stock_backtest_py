from multiprocessing import Pool

class Mulpro_Pool:

    def __init__(self,parm) -> None:
        pass
    def aync_calc(self,data,time):
        pass

if __name__ == "__main__":
    mulpro_Pool = Mulpro_Pool("parm")
    data = []
    time = None
    with Pool(processes=8) as pool:
        processed_data = pool.map(mulpro_Pool.aync_calc, (data,time))