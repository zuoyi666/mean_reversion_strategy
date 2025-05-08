import matplotlib.font_manager as fm

# 筛选出名字里带'PingFang'、'Hei'、'Songti'、'Arial Unicode'等关键字的字体
candidates = [f.name for f in fm.fontManager.ttflist
              if any(keyword in f.name for keyword in ['PingFang','Hei','Songti','Arial Unicode'])]
print(sorted(set(candidates)))
