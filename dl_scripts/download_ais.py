import wget
import os
import multiprocessing
import ais

def run_process(url, output_path):
    wget.download(url, out=output_path)
    # TODO: you can write your rename logic at here using os.rename

if __name__ == '__main__':
    print('retrieving ais links')
    ais_links = ais.get_links()

    cpus = multiprocessing.cpu_count()
    max_pool_size = 4
    pool = multiprocessing.Pool(cpus if cpus < max_pool_size else max_pool_size)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Folder names
    prefix_list = ["AIS"]
    download_list = []

    for prefix in prefix_list:
        path = os.path.join(base_dir, prefix)
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.isdir(path):
            exit()
        if prefix=="AIS":
            for name in ais_links:
                download_list.append([name, path])

    for url, path in download_list: # change here to download other files
        print('Beginning file download with wget module {n}'.format(n=url))
        pool.apply_async(run_process, args=(url, path, ))

    pool.close()
    pool.join()
    print("finish")