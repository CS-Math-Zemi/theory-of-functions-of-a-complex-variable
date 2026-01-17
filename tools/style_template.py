import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 図の全体サイズをかなり大きく設定 (幅24インチ, 高さ10インチ)
fig, axes = plt.subplots(1, 3, figsize=(24, 10))

# 共通の設定パラメータ
radius = 1.0
center = (0, 0)
arrow_start = (0.2, 0)  # 矢印の始点 (穴と被らないように少し右へ)
arrow_end = (0.9, 0)    # 矢印の終点

# カラー設定
fill_color = '#a0cbe2'  # 淡い水色
edge_color = 'black'
text_color = 'black'
hole_color = 'white'    # 穴の色

# フォントサイズ設定 (大きく変更)
math_fontsize = 40   # 下部の数式用
label_fontsize = 30  # 図の中のラベル(R, z0)用

# 各図のパラメータ設定
# (キャプションの数式, 塗りつぶし有無, 線のスタイル)
configs = [
    (r'$\Delta^{*}(z_0, R)$', True, '--'),        # 穴あき開円板
    (r'$\bar{\Delta}^{*}(z_0, R)$', True, '-'),   # 穴あき閉円板
    (r'$\partial\Delta(z_0, R)$', False, '-')     # 境界
]

for ax, (label, fill, style) in zip(axes, configs):
    # 1. 大きな円の描画
    circle = patches.Circle(
        center, 
        radius, 
        facecolor=fill_color if fill else 'none', 
        edgecolor=edge_color, 
        linestyle=style, 
        linewidth=4,   # 線を太く
        alpha=0.6 if fill else 1.0
    )
    ax.add_patch(circle)
    
    # --- 注釈の描画 (zorder=20で最前面) ---

    # 2. 半径 R の矢印とラベル
    ax.annotate(
        '', xy=arrow_end, xytext=arrow_start,
        arrowprops=dict(arrowstyle='<->', color='black', lw=3), zorder=20 # 矢印を太く
    )
    ax.text((arrow_start[0] + arrow_end[0])/2, -0.2, r'$R$', 
            ha='center', va='top', fontsize=label_fontsize, color=text_color, zorder=20)
    
    # 3. 中心点 z0 の穴（白抜き丸）の描画
    ax.scatter(*center, 
               facecolor=hole_color, 
               edgecolor='black', 
               s=250,         # 穴のサイズを大きく(前回80 -> 今回250)
               linewidth=3,   # 穴の枠線を太く
               zorder=20)     # 最前面
               
    ax.text(center[0], center[1] + 0.2, r'$z_0$', 
            ha='center', va='bottom', fontsize=label_fontsize, color=text_color, zorder=20)
    
    # --- レイアウト設定 ---
    # 4. キャプション（数式）を図の下に大きく表示
    ax.set_title(label, fontsize=math_fontsize, y=-0.2)

    # 軸の設定
    limit = 1.3
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect('equal')
    ax.axis('off')

# レイアウト調整 (下部の余白を大きく確保)
plt.subplots_adjust(bottom=0.25)
plt.show()