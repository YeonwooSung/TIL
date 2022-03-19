# Audio 플레이

자바스크립트로 오디오를 플레이하거나 HTML의 Audio tag를 통해 음악을 재생하는 기능을 구현하다 보면 다음 에러메세지를 만나게 된다.

"DOMException: play() failed because the user didn't interact with the document first"

이는 바뀐 브라우저 정책에 의해서 브라우저들이 오디오나 비디오의 자동 재생 등을 막기 위해 사용자에게 오디오나 비디오의 기능을 허용할 것인지를 먼저 묻도록 바뀌었기 때문이다. 실제로 설문조사 결과 대다수의 웹 사용자들이 자동 재생되는 음악이 user experience에 안 좋은 영향을 끼친다고 답했다고 한다. 바뀐 정책에 대한 자세한 설명은 [여기](https://developer.chrome.com/blog/autoplay/#webaudio)를 참조하기 바란다.

그래서 결론적으로, 이 에러를 해결하기 위해서는 따로 모달을 만들어서 사용자가 오디오 기능을 사용할지 물어보던가, 사용자가 브라우저 옵션에서 해당 페이지에 대해서 오디오 기능의 권한을 수락하던가, 아니면 오디오 기능에 대한 권한을 수락하도록 묻던가 해야 한다.

해결 방법에 대한 코드는 [여기](./audio_permission_for_autoplay.js)를 참조!
