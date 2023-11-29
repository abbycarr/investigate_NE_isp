import gzip
import shutil

fn = "/Users/abbycarr/Places_Things/investigate_NE_isp/data/intermediary/isp/att/kansas city/291650303054.geojson.gz"

with gzip.open(
    fn, "rb"
) as gz_in:
    with open(
        fn, "wb"
    ) as json_out:
        shutil.copyfileobj(gz_in, json_out)
