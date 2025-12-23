/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    const sleep = new Promise((resolve) => {
        setTimeout(resolve, millis);
    })
    return sleep;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */