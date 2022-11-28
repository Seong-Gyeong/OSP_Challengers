const imgPreview = document.querySelector(".imgPreview");

function getImageFiles(event) {
  const uploadedfiles = [];
  const files = event.target.files;
  console.log(files);
  console.log(typeof files, files);

  if ([...files].length >= 4) {
    alert("이미지는 최대 3개까지 업로드가 가능합니다.");
    return;
  }

  [...files].forEach((file) => {
    if ([...files].length < 4) {
      uploadedfiles.push(file);
      const reader = new FileReader();
      reader.onload = (e) => {
        const preview = createElement(e, file);
        imgPreview.appendChild(preview);
      };
      reader.readAsDataURL(file);
    }
  });

  console.log(uploadedfiles);
}

function createElement(event, file) {
  const li = document.createElement("li");
  const img = document.createElement("img");
  img.setAttribute("src", event.target.result);
  img.setAttribute("data-file", file.name);
  li.appendChild(img);

  return li;
}

const imgInput = document.querySelector(".imgInput");
const upload = document.querySelector(".upload");

// 파일 업로드 버튼을 클릭하지 않고 div 영역을 클릭했을 때 사진 고르는 창이 나오도록 함
upload.addEventListener("click", () => imgInput.click());

imgInput.addEventListener("change", getImageFiles);
