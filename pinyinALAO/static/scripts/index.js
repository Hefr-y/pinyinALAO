console.log('Le script est bien chargé!');


// 点击按钮后生成拼音数据的方法函数
function pyInfo() {

    // 获取用户输入
    var hanziInput = document.getElementById('hanziInput').value;

    // var pinyinInfo = cnchar.spell(hanziInput,"array")

    var pinyinInfoWithTone = cnchar.spell(hanziInput,"array",'tone');

    var pinyinOut = document.getElementById("pinyinOut");
    var pinyinOutWithTone = document.getElementById("pinyinOutWithTone");
    pinyinOutWithTone.innerHTML = "";
    pinyinOut.innerHTML = "";
    pinyinOutWithTone.innerHTML = "pinyin with tone:  " + pinyinInfoWithTone;


    for (pinyinNum in pinyinInfoWithTone) {
        var pyDetails = cnchar.spellInfo(pinyinInfoWithTone[pinyinNum]);
        console.log(pyDetails);

        for(var key in pyDetails){
            var pyValue = pyDetails[key];
            // console.log(pyValue);
            var pinyinOut = document.getElementById("pinyinOut")
            pinyinOut.innerHTML += key + ":" + pyValue + '<br/>';
        }
        pinyinOut.innerHTML +=  '<br/>';
    }

    // console.log(pinyinInfo,pinyinInfoWithTone,pyDetail);

    // document.getElementById("pinyinOut").innerHTML = "pinyin sans tone:  " + pinyinInfo;


}


async function sendText() {

    // ON RÉCUPÈRE LES VARIABLES À ENVOYER AU SERVEUR

    var inText = document.getElementById('inText').value;



    // ON EMBALLE TOUT ÇA DANS UN JSON

    var colis = {

        inText: inText

    }

    console.log('Envoi colis:',colis);


    // PARAMÈTRES DE LA REQUÊTE

    const requete = {

        method: 'POST',

        headers: {

            'Content-Type': 'application/json'

        },

        body: JSON.stringify(colis)

    };


    // ENVOI ET RÉCUPÉRATION DE LA RÉPONSE
    const response = await fetch('/hsk1/', requete);
    const data = await response.json();
    console.log(data);

//     var outText = document.getElementById('outText');
//     outText.innerHTML = ""; // vider la div si elle contenait déjà qqc
//     for (token in data.reponse) {
//         var tokenTuple = data.reponse[token];
//         console.log(tokenTuple[0], tokenTuple[1]);
//         outText.innerHTML += tokenTuple[0] + ' : ' + tokenTuple[1] + '<br/>';
//   }

}