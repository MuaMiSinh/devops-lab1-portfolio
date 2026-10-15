# Lab 1: Trải nghiệm DevOps Workflow End-to-End

## Bài thực hành đã hoàn thành

- **Họ tên sinh viên:** Mua Mí Sính
- **MSSV:** DTC235180159
- **Lớp:** KTPM K22C
- **Bộ bài nộp:** [Lab1 - **Mua Mí Sính - DTC235180159**](<Lab1 - Mua Mí Sính - DTC235180159/README.md>)
- **Báo cáo:** [Báo cáo Lab 1](<Lab1 - Mua Mí Sính - DTC235180159/BaoCao_Lab1.md>)
- **Kết quả CI/CD:** [Hai lần triển khai thành công](<Lab1 - Mua Mí Sính - DTC235180159/KetQua_ThucHanh.md>)
- **Ảnh minh chứng:** [screenshots](<Lab1 - Mua Mí Sính - DTC235180159/screenshots/>)
- **Mã nguồn website:** [index.html](../../index.html)
- **Pipeline:** [deploy.yml](../../.github/workflows/deploy.yml)
- **Website online:** https://muamisinh.github.io/devops-lab1-portfolio/
- **URL nộp bài Lab 1:** https://github.com/MuaMiSinh/devops-lab1-portfolio/tree/main/Labs/B%C3%A0i%201

Phần bên dưới là hướng dẫn gốc của bài thực hành.

## Thông tin chung
- **Bài học 1:** Tổng quan về Vận hành & Bảo trì Phần mềm
- **CDR:** 1.2 (Hiểu DevOps vs truyền thống) + 1.3 (Hiểu vòng đời DevOps)
- **Mức Bloom:** Hiểu + Vận dụng cơ bản
- **Thời lượng:** 60 phút
- **Hình thức:** Sinh viên tự thực hành

## Mục tiêu
Sau lab này, sinh viên có thể:
1. Trải nghiệm **toàn bộ vòng đời DevOps**: Plan → Code → Build → Test → Deploy → Monitor
2. Tự tay tạo CI/CD pipeline với **GitHub Actions** (miễn phí)
3. Deploy website tĩnh lên **GitHub Pages** và xem kết quả trực tuyến
4. So sánh quy trình DevOps tự động với cách làm thủ công truyền thống

## Tại sao chọn GitHub Actions + GitHub Pages?
- **Hoàn toàn miễn phí** — không cần tài khoản cloud, không cần thẻ tín dụng
- **Thể hiện rõ DevOps flow**: push code → CI chạy → deploy tự động
- **Visual Pipeline** — GitHub UI hiển thị từng step

## Kịch bản Lab
Bạn là developer trong 1 team nhỏ. Bạn được giao tạo **trang giới thiệu cá nhân** (portfolio) và tự động hóa việc deploy mỗi khi cập nhật code. Bạn sẽ:
1. Tạo web tĩnh HTML/CSS đơn giản
2. Thiết lập GitHub Actions pipeline tự động test & deploy
3. Push code → quan sát CI/CD tự động chạy → xem website online

## Nội dung Lab
| Step | Nội dung | Thời gian |
|------|----------|-----------|
| 1 | Tạo GitHub Repository + Web tĩnh | 15 phút |
| 2 | Viết GitHub Actions CI/CD Pipeline | 15 phút |
| 3 | Push Code & Quan sát Pipeline | 15 phút |
| 4 | So sánh DevOps vs Truyền thống | 15 phút |
=> Hướng dẫn chi tiết: Sinh viên xem file: Lab1_HuongDan.
Chúc bạn học và thực hành tốt bài Lab1
