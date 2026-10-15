# Lab 2: Thiết lập Môi trường DevOps & Áp dụng Nguyên tắc CALMS

## Bài thực hành đã hoàn thành

- **Họ tên sinh viên:** Mua Mí Sính
- **MSSV:** DTC235180159
- **Lớp:** KTPM K22C
- **Bộ bài nộp:** [Lab2 - **Mua Mí Sính - DTC235180159**](<Lab2 - Mua Mí Sính - DTC235180159/README.md>)
- **Báo cáo và đánh giá CALMS:** [Báo cáo Lab 2](<Lab2 - Mua Mí Sính - DTC235180159/BaoCao_Lab2.md>)
- **Script tự động hóa:** [setup-dev-env.ps1](<Lab2 - Mua Mí Sính - DTC235180159/setup-dev-env.ps1>)
- **Cấu hình Docker:** [Dockerfile](<Lab2 - Mua Mí Sính - DTC235180159/Dockerfile>)
- **Ảnh minh chứng và sơ đồ:** [screenshots](<Lab2 - Mua Mí Sính - DTC235180159/screenshots/>)
- **Log thực hành:** [logs](<Lab2 - Mua Mí Sính - DTC235180159/logs/>)
- **File ZIP:** [Lab2_MuaMiSinh_DTC235180159.zip](Lab2_MuaMiSinh_DTC235180159.zip)
- **URL bài Lab 2:** https://github.com/MuaMiSinh/devops-lab1-portfolio/tree/main/Labs/B%C3%A0i%202

Script setup và Docker build/run đã được kiểm tra; chi tiết nằm trong báo cáo và log. Ảnh 01–04 là bản trình bày từ log thực tế, không phải ảnh chụp màn hình terminal. Bảng tự đánh giá CALMS là đề xuất để sinh viên xác nhận.

Phần bên dưới là hướng dẫn gốc của bài thực hành.

## Thông tin chung
- **Bài 2 — DevOps và các Nguyên tắc Cốt lõi** 
- **CDR:** 2.1 (Khái niệm DevOps) + 2.2 (Nguyên tắc cốt lõi) + 2.3 (Công cụ DevOps)
- **Mức Bloom:** Hiểu + Vận dụng cơ bản
- **Thời lượng:** 75 phút
- **Hình thức:** Sinh viên tự thực hành theo hướng dẫn

## Mục tiêu
Sau lab này, sinh viên có thể:
1. Cài đặt và cấu hình **DevOps Toolchain** cơ bản: VS Code + Git + Docker Desktop
2. Hiểu và áp dụng **5 nguyên tắc CALMS** qua bài tập thực hành
3. Tạo **automation script** đầu tiên — nguyên tắc Automation của DevOps
4. Vẽ được **DevOps Toolchain Map** — biết công cụ nào dùng cho giai đoạn nào

## CALMS Framework

<p align="center">
  <img src="images_Lab2/1_calms.png" alt=" CALMS Framework" width="600">
</p>



## Nội dung Lab
| Step | Nội dung | CALMS | Thời gian |
|------|----------|:-----:|-----------|
| 1 | Cài đặt DevOps Toolchain | — | 20 phút |
| 2 | Automation: Script tự động hóa đầu tiên | A | 15 phút |
| 3 | Lean: Tối ưu quy trình với Docker | L | 15 phút |
| 4 | DevOps Toolchain Map + Tổng kết | M+S | 15 phút |
| 5 | CALMS Self-Assessment | C+M+S | 10 phút |
