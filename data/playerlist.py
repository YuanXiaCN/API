# -*- coding: gbk -*-
import tkinter as tk
from tkinter import filedialog

# �����Ի���
root = tk.Tk()
root.withdraw()

# ����ѡ���ļ��Ի���
log_file = filedialog.askopenfilename(title="ѡ����־�ļ�")

# ����־�ļ�����ȡ����
try:
 with open(log_file, "r", encoding="gbk") as file:
    log_data = file.read()
    # ������־����
    # ����������Ը��ݾ������������־������ȡ��Ϣ�Ȳ���
    # ���磬����԰��в����־��ͳ�ƹؼ��ʳ��ֵĴ����ȵ�

    # ��������Ľ��
    print(log_data)

except FileNotFoundError:
    print("�Ҳ���ָ������־�ļ�������·���Ƿ���ȷ��")