function addPersonMethods(def){
    var obj = {
        name:def['name'],
        age:def['age'],
        greet : function(greeting){
         console.log(greeting+", my name is " + this.name);
     },
        compareAge :function (otherpeople) {
            if (this.age == otherpeople.age){
                console.log("My name is " + this.name+" and I'm equally young as "+otherpeople.name);
            }
            if(this.age>otherpeople.age){
                console.log("My name is " + this.name+" and I'm older than "+otherpeople.name);
            }
            if(this.age<otherpeople.age){
                console.log("My name is " + this.name+" and I'm younger than "+otherpeople.name);
            }
        },
        namesake : function (otherpeople) {
            if(this.name == otherpeople.name){
                console.log("We have the same name, "+otherpeople.name+" and I!");
            }
            else {
                console.log("We have different names, "+otherpeople.name+" and I.");
            }
        }
    }
    return obj;
}
