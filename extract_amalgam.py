import io
import sys
import zipfile


def main(path):
    zf = zipfile.ZipFile(path)
    print("Extracting from %r" % path)
    print("\n".join(zf.namelist()))
    infos = []
    for info in zf.filelist:
        if info.filename.endswith("sqlite3.c"):
            infos.append(info)
        if info.filename.endswith("sqlite3ext.h"):
            infos.append(info)
        if info.filename.endswith("sqlite3.h"):
            infos.append(info)
    for info in infos:
        print("Extracting %r..." % info.filename)
        content = zf.read(info)
        with open(info.filename.split("/")[-1], 'wb') as fh:
            fh.write(content)


if __name__ == "__main__":
    path = sys.argv[1]
    main(path)
