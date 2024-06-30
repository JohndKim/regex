import React, { useState } from 'react';
import { useAppDispatch, useAppSelector } from '../hooks';
import { fetchGrepData } from '../features/grepSlice';

const Grepper: React.FC = () => {
    // states for input fields
    const [string, setString] = useState(''); 
    const [regex, setRegex] = useState('');

    // redux states and dispatch
    const { loading, data, error } = useAppSelector((state) => state.grep);
    const dispatch = useAppDispatch();

    // handle form submission
    const handleSubmit = () => {
        console.log(string, regex);
        dispatch(fetchGrepData({ string, regex }));
    }

    return (
        <div className="x">
            <header>Hello</header>
            <input 
                type="text" 
                placeholder="string" 
                value={string}
                onChange={(e) => setString(e.target.value)} 
            />
            <input 
                type="text" 
                placeholder="regex" 
                value={regex}
                onChange={(e) => setRegex(e.target.value)} 
            />
            <button onClick={handleSubmit}>Submit</button>
            
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error}</p>}
            {data && (
                <div>
                    <p>Status: {data.status.toString()}</p>
                    <p>NFA: {JSON.stringify(data.nfa)}</p>
                    <p>Path: {JSON.stringify(data.path)}</p>
                </div>
            )}
        </div>
    );
}

export default Grepper;



// import { useSelector, useDispatch } from "react-redux";
// import { RootState } from "../store";
// import { useEffect, useState } from 'react';
// import { useAppDispatch, useAppSelector } from '../hooks';
// import { fetchGrepData } from '../features/grepSlice'


// const Grepper = () => {
//     // SETTING STATES
//     const [string, setString] = useState('') 
//     const [regex, setRegex] = useState('')

//     // REDUX
//     // const grep = useAppSelector((state: RootState) => state.grep)
//     const { loading, data, error } = useAppSelector((state) => state.grep);
//     // const dispatch = useDispatch();
//     const dispatch = useAppDispatch();

//     const handleSubmit = () => {
//         console.log(string, regex)
//         dispatch(fetchGrepData({string: string, regex: regex}));
//         console.log(loading, data, error)
//     }
    
//     return (
//         <div className="x">
//             <header>hello
//             </header>
//             <input type="text" placeholder="string" onChange={(e) => setString(e.target.value)}></input>
//             <input type="text" placeholder="regex" onChange={(e) => setRegex(e.target.value)}></input>
//             <button onClick={handleSubmit}></button>

//             {/* <p>{data.nfa}</p> */}
//         </div>
//     )
// }

// export default Grepper;