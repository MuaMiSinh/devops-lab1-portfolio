"""Tạo hình bảng so sánh và sơ đồ học tập; ảnh GitHub được chụp riêng từ trình duyệt."""
from pathlib import Path
import textwrap
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent / 'screenshots'
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 23)
bold = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 24)
title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 33)
image = Image.new('RGB', (1550, 1000), '#f2f5fa')
draw = ImageDraw.Draw(image)
draw.text((40, 25), 'LAB 1 — DEVOPS VÀ QUY TRÌNH TRUYỀN THỐNG', font=title, fill='#24385b')
draw.text((40, 78), 'Mua Mí Sính · DTC235180159 · KTPM K22C · 15/10/2026', font=font, fill='#465673')
rows = [
    ('Tiêu chí', 'Thủ công (Traditional)', 'DevOps (CI/CD)'),
    ('Triển khai', 'Chép mã, upload và cấu hình bằng tay.', 'Push main → kiểm tra → build → cập nhật gh-pages → Pages.'),
    ('Thời gian', 'Ví dụ giáo trình: 15–30 phút. Chưa đo thực nghiệm.', 'CI: 13s / 11s. Pages tiếp theo: 22s / 23s. Còn thời gian chờ.'),
    ('Ai thực hiện?', 'Developer hoặc người vận hành thao tác từng bước.', 'Runner thực hiện quy trình do con người cấu hình.'),
    ('Sai sót', 'Có thể bỏ bước, nhầm tệp hoặc cấu hình.', 'Giảm lỗi thao tác; vẫn có thể lỗi mã, cấu hình hoặc dịch vụ.'),
    ('Rollback', 'Tìm và upload bản sao cũ.', 'git revert <commit> rồi push main; chờ deploy và kiểm tra lại.'),
    ('Xác nhận', 'Kiểm tra tệp, log và website bằng tay.', 'Actions + trạng thái Pages + nội dung website online.'),
]
widths = [240, 590, 640]
y = 135
for row_index, row in enumerate(rows):
    x = 40
    height = 75 if row_index == 0 else 112
    for cell_index, cell in enumerate(row):
        draw.rectangle((x, y, x + widths[cell_index], y + height), fill='#24385b' if row_index == 0 else ('#ffffff' if row_index % 2 else '#e8eef8'), outline='#cbd5e1')
        lines = textwrap.wrap(cell, width=[16, 43, 46][cell_index])
        for line_index, line in enumerate(lines):
            draw.text((x + 15, y + 15 + line_index * 29), line, font=bold if row_index == 0 else font, fill='white' if row_index == 0 else '#24385b')
        x += widths[cell_index]
    y += height
draw.text((40, 925), 'Số liệu CI/Pages lấy từ run thật; chưa có phép đo triển khai thủ công tương đương.', font=font, fill='#465673')
image.save(root / '06-comparison-table.png')

image = Image.new('RGB', (1550, 1040), '#102033')
draw = ImageDraw.Draw(image)
draw.text((40, 28), 'DEVOPS WORKFLOW — LAB 1', font=title, fill='#6ee7cf')
lines = [
    'PLAN — Xác định trang portfolio và tiêu chí chấm',
    '↓',
    'CODE — HTML/CSS → Git commit → push main',
    '↓',
    'TEST — GitHub Actions: Python kiểm tra HTML và thông tin sinh viên',
    '↓',
    'BUILD — Tạo _site/ chỉ chứa website và .nojekyll',
    '↓',
    'DEPLOY — Action cập nhật gh-pages → GitHub Pages build và phục vụ',
    '↓',
    'MONITOR — Kiểm tra Actions, HTTP 200 và giao diện online',
    '↓',
    'FEEDBACK — Sửa tiêu đề tiếng Việt → push → pipeline chạy lại',
    '',
    'Khôi phục khi lỗi: git revert <commit> → push main → kiểm tra deploy mới.',
    'Build ở bài web tĩnh là đóng gói; test chạy trước để phát hiện lỗi sớm.',
    '',
    'Mua Mí Sính · DTC235180159 · KTPM K22C',
]
for index, line in enumerate(lines):
    draw.text((40, 110 + index * 48), line, font=font, fill='#edf3fc')
image.save(root / '07-devops-workflow.png')
