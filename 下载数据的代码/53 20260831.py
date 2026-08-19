import cdsapi
import os

# =====================================================
# 保存目录
# =====================================================

SAVE_DIR = "/Users/zhangnan/日常文件/ai/每周下载和预测/53 20260831/数据/download"

os.makedirs(SAVE_DIR, exist_ok=True)

# =====================================================
# 下载日期
# =====================================================

YEAR = "2026"
MONTH = ["08"]

DAYS = [
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
]

# =====================================================
# CDS Client
# =====================================================

c = cdsapi.Client()

# =====================================================
# Pressure Level 数据
# =====================================================

pressure_jobs = [

    (
        "geopotential",
        "200",
        "ERA5-daily-200hpa-Geopotential-20260831.nc"
    ),

    (
        "geopotential",
        "300",
        "ERA5-daily-300hpa-Geopotential-20260831.nc"
    ),

    (
        "geopotential",
        "500",
        "ERA5-daily-500hpa-Geopotential-20260831.nc"
    ),

    (
        "specific_humidity",
        "700",
        "ERA5-daily-700hPa-SpecificHumidity-20260831.nc"
    ),

    (
        "fraction_of_cloud_cover",
        "800",
        "ERA5-daily-800hPa-CloudFraction-20260831.nc"
    ),

    (
        "geopotential",
        "850",
        "ERA5-daily-850hpa-Geopotential-20260831.nc"
    ),

    (
        "divergence",
        "900",
        "ERA5-daily-900hPa-Divergence-20260831.nc"
    ),

    (
        "potential_vorticity",
        "900",
        "ERA5-daily-900hPa-PotentialVorticity-20260831.nc"
    ),
]

# =====================================================
# 下载 Pressure Levels
# =====================================================

for variable, level, filename in pressure_jobs:

    outfile = os.path.join(SAVE_DIR, filename)

    print(f"\nDownloading: {filename}")

    c.retrieve(
        "derived-era5-pressure-levels-daily-statistics",
        {
            "product_type": "reanalysis",
            "variable": [variable],
            "pressure_level": [level],

            "year": YEAR,
            "month": MONTH,
            "day": DAYS,

            "daily_statistic": "daily_mean",
            "time_zone": "utc+08:00",
            "frequency": "6_hourly",

            "data_format": "netcdf",
        },
        outfile,
    )

# =====================================================
# Single Level 数据
# =====================================================

single_jobs = [

    (
        "2m_temperature",
        "daily_mean",
        "6_hourly",
        "ERA5-daily-single level-2m_Temperature-20260831.nc"
    ),

    (
        "mean_sea_level_pressure",
        "daily_mean",
        "6_hourly",
        "ERA5-daily-single level-MSLP-20260831.nc"
    ),

    (
        "total_precipitation",
        "daily_sum",
        "1_hourly",
        "ERA5-daily-single level-Totalprecipiation-20260831.nc"
    ),
]

# =====================================================
# 下载 Single Levels
# =====================================================

for variable, statistic, frequency, filename in single_jobs:

    outfile = os.path.join(SAVE_DIR, filename)

    print(f"\nDownloading: {filename}")

    c.retrieve(
        "derived-era5-single-levels-daily-statistics",
        {
            "product_type": "reanalysis",
            "variable": [variable],

            "year": YEAR,
            "month": MONTH,
            "day": DAYS,

            "daily_statistic": statistic,
            "time_zone": "utc+08:00",
            "frequency": frequency,

            "data_format": "netcdf",
        },
        outfile,
    )

print("\n===================================")
print("ERA5 Daily 数据全部下载完成")
print("保存目录：")
print(SAVE_DIR)
print("===================================")