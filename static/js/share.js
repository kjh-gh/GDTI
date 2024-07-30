let nowUrl = window.location.href;

function copyUrl(){ 
  //nowUrl 변수에 담긴 주소를
  	navigator.clipboard.writeText(nowUrl).then(res=>{
	  alert("URL 복사가 완료되었습니다");
	})
}

/*------------------------------------------------------------------------*/
