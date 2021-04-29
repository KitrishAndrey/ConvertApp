function animateGrid() {

      anime({
      targets: '.stagger-visualizer .anim-row',
      scale: [
      {value: .1, easing: 'easeOutSine', duration: 500},
      {value: 1, easing: 'easeInOutQuad', duration: 1200}
      ],
      delay: anime.stagger(200, {grid: [13, 1], from: 'center'})
          });
          }

async function ConvertMainFunc() {
    var folder_path = document.getElementById("folderpath").value;
    console.log(folderpath);
    var res = await eel.ConvertMainFunc(folder_path)();
    document.getElementById("outputlist").innerHTML=res;

    var counter = await eel.GetCounter()();
    document.getElementById("nfiles").innerHTML="Number of converted files" + " " + counter;

};
document.querySelector(".button").onclick = function(){
    animateGrid();
    ConvertMainFunc();
}

