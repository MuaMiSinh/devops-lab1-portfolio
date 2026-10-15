# VHBTPM_DevOps_2026
Kho này trợ giúp sinh viên trong quá trình học khóa học Vận hành và Bảo trì phần mềm với DevOps

DTC235180159 - Mua Mí Sính - KTPM K22C

## Lab 1 — Portfolio và CI/CD

- Website: https://muamisinh.github.io/devops-lab1-portfolio/
- Pipeline: https://github.com/MuaMiSinh/devops-lab1-portfolio/actions
- Mã web: `index.html`; pipeline: `.github/workflows/deploy.yml`.
- Kiểm tra tại máy: `python scripts/validate-lab1.py`, sau đó mở `index.html` trong trình duyệt.

Đẩy thay đổi lên `main` để GitHub Actions kiểm tra HTML, tạo `_site/` và tự xuất bản nội dung sang `gh-pages`. GitHub Pages phục vụ nhánh `gh-pages` tại thư mục gốc. Chỉ `index.html` và `.nojekyll` được xuất bản; tài liệu các lab không nằm trong artifact website.

Để quay lại nội dung cũ, dùng `git revert <commit>` rồi push `main`. Theo dõi Actions và mở website để kiểm tra kết quả thực tế.
