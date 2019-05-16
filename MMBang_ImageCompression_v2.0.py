# -*- coding: utf-8 -*
import tinify
import os
import shutil

# 设置超过 50kb 的图片才会被压缩,此数值可以自由设置
MIN_SIZE = 1024 * 50

# 配置可被压缩的 图片类型，可添加其他图片类型
IMAGE_TYPE_LIST = ['.jpg', '.png']

"""
    1. Developer API Key地址：进入https://tinypng.com/dashboard/developers网址后选择Developer API
    2. API地址：https://tinypng.com/developers/reference/python
    3. 免费用户每个key每个月最多只能压500次，可通过多注册几个邮箱的方式解决次数的限制
"""
KEY_LIST = [
    "5d9Gyl9jdrBUA4ta3vjsaJivOS2hWc3I",
    "CamGjDuqeG2FxOE2RsEQhhZa1XGN1MfV",
]
online_key_list_iter = iter(KEY_LIST)
total_file = 0


def iterate_file(src_path):
    global total_file
    result = False
    for path, dirs, files in os.walk(src_path):
        if len(files) > 0:
            # 遍历文件
            for file in files:
                new_file_path = os.path.join(path, file)
                file_name, file_suffix = os.path.splitext(file)
                if file_suffix in IMAGE_TYPE_LIST:
                    size = os.path.getsize(new_file_path)
                    # 如果图片文件大于指定大小的话就进行tinyPNG压缩，否则就不压缩
                    if size > MIN_SIZE:
                        total_file += 1
                        # 调用tiny的api对图片进行压缩
                        try:
                            source = tinify.from_file(new_file_path)
                            if os.path.exists(new_file_path):
                                os.remove(new_file_path)
                            # 压缩完成后会直接覆盖原来的图片文件，想寻找压缩前的图片可到根目录的backup文件夹下寻找
                            source.to_file(new_file_path)
                            print("===第 %s 个图片压缩成功，图片名：%s" % (total_file, new_file_path))
                            result = True
                            pass
                        except tinify.AccountError as e:
                            print("当前key值无效，将自动更换可用key值后继续压缩 %s" % e.message)
                            tinify.key = next(online_key_list_iter)
                            source = tinify.from_file(new_file_path)
                            if os.path.exists(new_file_path):
                                os.remove(new_file_path)
                            # 压缩完成后会直接覆盖原来的图片文件，想寻找压缩前的图片可到根目录的backup文件夹下寻找
                            source.to_file(new_file_path)
                            print("===第 %s 个图片压缩成功，图片名：%s" % (total_file, new_file_path))

                        except tinify.ClientError as e:
                            # Check your source image and request options.
                            print("Check your source image and request options. %s" % e.message)
                            result = False
                            pass
                        except tinify.ServerError as e:
                            # Temporary issue with the Tinify API.
                            print("Temporary issue with the Tinify API. %s" % e.message)
                            result = False
                            pass
                        except tinify.ConnectionError as e:
                            # A network connection error occurred.
                            print("网络故障,程序将在10秒后继续尝试连接 %s" % e.message)
                            result = False
                            pass

        # 遍历文件夹
        """
        if len(dirs) > 0:
            for dir_name in dirs:
                new_dir_path = os.path.join(src_path, dir_name)
                iterate_file(new_dir_path)
        """
    print("=====压缩完成，本次总计压缩 %s 个图片文件" % total_file)
    return result


def begin_compress_image(src_path, backup_path):
    tinify.key = KEY_LIST[0]
    # 创建备份文件目录
    final_backup_path = os.path.join(backup_path, "backup")
    if os.path.exists(final_backup_path):
        shutil.rmtree(final_backup_path)
        shutil.copytree(src_path, final_backup_path)

    else:
        final_backup_path = os.path.join(backup_path, "backup")
        os.mkdir(final_backup_path)
        shutil.rmtree(final_backup_path)
        # 开始备份原始图片文件夹
        shutil.copytree(src_path, final_backup_path)
    # 遍历图片资源文件夹，开始压缩文件shutil.copytree
    iterate_file(src_path)


if __name__ == "__main__":
    print("开始路径配置")
    src_root = input("请指定图片源文件夹地址：")
    desc_root = input("请指定图片文件备份地址：")
    begin_compress_image(src_root, desc_root)
