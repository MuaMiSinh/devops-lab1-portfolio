"""Render recorded command output as PNG; these are log illustrations, not screen captures."""
from pathlib import Path
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONT = 'C:/Windows/Fonts/arial.ttf'
MONO = 'C:/Windows/Fonts/consola.ttf'

def render(name, title, lines, mono=False):
    font = ImageFont.truetype(MONO if mono else FONT, 22)
    wrapped = []
    for line in lines:
        wrapped.extend(textwrap.wrap(line, width=108) or [''])
    image = Image.new('RGB', (1500, max(380, 150 + len(wrapped) * 32)), '#102033')
    draw = ImageDraw.Draw(image)
    draw.text((35, 25), title, font=ImageFont.truetype(FONT, 30), fill='#6ee7cf')
    for i, line in enumerate(wrapped):
        draw.text((35, 95 + i * 32), line, font=font, fill='#edf3fc')
    image.save(ROOT / 'screenshots' / name)

for stem in ['01-toolchain-check', '02-automation-script', '03-docker-build', '04-docker-run-curl']:
    path = ROOT / 'logs' / (stem + '.txt')
    raw = path.read_bytes()
    content = raw.decode('utf-16' if raw.startswith((b'\xff\xfe', b'\xfe\xff')) else 'utf-8-sig', errors='replace')
    render(stem + '.png', 'LAB 2 | Bản trình bày log thực tế | ' + stem, content.splitlines(), True)

render('05-toolchain-map.png', 'DEVOPS TOOLCHAIN MAP — Mua Mí Sính — DTC235180159', [
    '01 PLAN       GitHub Projects: quản lý task, roadmap',
    '       ↓',
    '02 CODE       VS Code · Git · GitHub: soạn mã, quản lý phiên bản, cộng tác',
    '       ↓',
    '03 BUILD      npm · Maven · Docker: dependencies, build, đóng gói',
    '       ↓',
    '04 TEST       Postman · Newman · SonarQube · OWASP ZAP: chất lượng, bảo mật',
    '       ↓',
    '05 RELEASE    Nexus · Docker Hub: lưu trữ artifact, image',
    '       ↓',
    '06 DEPLOY     Docker · Terraform · AWS: triển khai ứng dụng, hạ tầng',
    '       ↓',
    '07 OPERATE    Docker Engine: container, trạng thái, logs',
    '       ↓',
    '08 MONITOR    Prometheus · Grafana: metrics, dashboard → phản hồi về PLAN',
    '',
    'CI/CD xuyên suốt Build → Test → Deploy: GitHub Actions · Jenkins',
    'Lab 2 thực hành: VS Code, Git, npm, Docker. Các công cụ khác: ánh xạ giáo trình/mở rộng.'
])
render('06-calms-assessment.png', 'CALMS SELF-ASSESSMENT — Đề xuất để sinh viên xác nhận', [
    'Mua Mí Sính | DTC235180159 | KTPM K22C | 15/10/2026',
    '',
    'Culture          2/5    Có tài liệu; chưa kiểm chứng cộng tác Dev/Ops.',
    'Automation    3/5    Có script setup; chưa có pipeline đầy đủ.',
    'Lean               4/5    Dùng Docker và script; phụ thuộc mạng khi tải image.',
    'Measurement 2/5    Có log và thời gian; chưa có dashboard/alert.',
    'Sharing           3/5    Có báo cáo, sơ đồ; chưa kiểm chứng code review nhóm.',
    'TỔNG            14/25',
    '',
    '1. Tuần tới: thêm GitHub Actions kiểm tra cú pháp và build image cho pull request.',
    '2. Hai buổi tới: thêm health check, đo thời gian setup/build qua ít nhất ba lần.',
    '3. Buổi nhóm tới: nhờ bạn chạy lại, đo onboarding và tạo pull request có review.'
])
