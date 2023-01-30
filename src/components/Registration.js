import React, {useState} from 'react';

function NewAccountInfo() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    return (
        <form>
            <fieldset>
                <legend>Enter your name and email:</legend>

                <label>Name:
                    <input type="text" value={name}
                     onChange={e => setName(e.target.value)} />
                </label>
                
                <br/>

                <label>Email:
                    <input type="text" value={email}
                     onChange={e => setEmail(e.target.value)} />
                </label>
                
                <br/>

                <button onClick={e => {
                    alert(`Thank you for making an account with LegitMart, ${name}! Your exclusive promotions and coupons will be sent to ${email}.`);
                    e.preventDefault();
                }}>Submit</button>
            </fieldset>
        </form>
    );
}

export default NewAccountInfo;