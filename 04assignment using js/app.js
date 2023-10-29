class Toyota {
    type() {
        throw new Error("Метод speak должен быть реализован.");
    }
}

class Camry extends Toyota {
    type() {
        return "V8 Engine";
    }
}

class Corolla extends Toyota {
    type() {
        return "V6 Engine";
    }
}

class ToyotaFactory {
    createToyota(toyotaType) {
        switch (toyotaType) {
            case "Camry":
                return new Camry();
            case "Corolla":
                return new Corolla();
            default:
                throw new Error("Такого нету.");
        }
    }
}

const factory = new ToyotaFactory();

const camry = factory.createToyota("Camry");
const corolla = factory.createToyota("Corolla");

console.log(camry.type());
console.log(corolla.type());
