

function getPromise1() {
    return new Promise((resolve, reject) => {
        setTimeout(()=> {
            resolve('done');
        }, 1000);
    });
}

function getPromise2(message) {
    return new Promise((resolve, reject) => {
        setTimeout(()=> {
            resolve(message + ' done');
        }, 1000);
    });
}

const testPromise = async () => {
    try {
        const result = await getPromise1();
        console.log(result);
    } catch (error) {
        console.log(error);
    }
}

testPromise();
// done
// done

getPromise1()
    .then(result => {
        console.log(result); return result;
    })
    .then(result => getPromise2(result))
    .then(result2 => console.log(result2))
    .catch(error => console.log(error))
// done done
