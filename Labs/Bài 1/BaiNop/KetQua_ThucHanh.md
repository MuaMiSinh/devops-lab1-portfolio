# Kết quả thực hành — 15/10/2026

| Lần | Commit main | CI tự động | GitHub Pages tiếp theo | Kết quả |
|---|---|---|---|---|
| Hoàn thiện portfolio | `67eab5d` | [Run 38721116527](https://github.com/MuaMiSinh/devops-lab1-portfolio/actions/runs/38721116527), 13 giây | [Run 38721139719](https://github.com/MuaMiSinh/devops-lab1-portfolio/actions/runs/38721139719), 22 giây | Cả hai success |
| Đổi tiêu đề tiếng Việt | `2586385` | [Run 38721502925](https://github.com/MuaMiSinh/devops-lab1-portfolio/actions/runs/38721502925), 11 giây | [Run 38721521581](https://github.com/MuaMiSinh/devops-lab1-portfolio/actions/runs/38721521581), 23 giây | Cả hai success |

Website trả HTTP 200 và hiển thị **Xin chào, DevOps!**, **Lab 1 — Website đã được cập nhật tự động!**, Mua Mí Sính, DTC235180159, KTPM K22C. Thời gian ở bảng là từng run, không bao gồm toàn bộ thời gian lan truyền cache hay mọi khoảng chờ giữa các run.

Kiểm tra tại máy: script HTML đạt; thử bỏ MSSV trong bản sao tạm thì script phát hiện lỗi; `git diff --check` đạt. Kiểm tra trình duyệt xác nhận ngày xem, tiêu đề và thông tin cá nhân hiển thị đúng.

GitHub có cảnh báo runtime Node.js của các action mẫu cũ đang được runner chuyển sang Node.js 24; các run vẫn thành công. Bài giữ các action theo cấu trúc giáo trình, chưa thực hiện nâng cấp action ngoài phạm vi bài.
