var crypto = require('crypto');

function md5(str1, str2) {
  var md5sum = crypto.createHash('md5');
  md5sum.update(str1 + str2);
  var d = md5sum.digest('hex');
  //console.log(d);
  return d;
}

function countCode(password, key){
  if(password && key){
    var md5one = md5(password,key);
    var md5two = md5(md5one,'long');
    var md5three = md5(md5one,'chang');
    //计算大小写
    var rule = md5three.split("");
    var source = md5two.split("");
    //console.warn('rule', rule);
    //console.warn('source', source);
    for(var i=0;i<=31;i++){ 
      if(isNaN(source[i])){
        str ="longchang1990def";
        //console.log(i, source[i], isNaN(source[i]), rule[i], str.search(rule[i]));
        if(str.search(rule[i]) > -1){
          source[i] = source[i].toUpperCase();
        }
      }
    }
    var code32 = source.join("");
    var code1 = code32.slice(0,1);
    if(isNaN(code1)){
      var code16 = code32.slice(0,16);
    }else{
      var code16 = "L" + code32.slice(1,16);
    }
    console.log(code16);
    //$("#code16").text(code16);
    return code16;
  }
}

countCode('123456', 'qq');
countCode('123456', ' ');
