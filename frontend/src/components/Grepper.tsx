import React, { useState, useEffect } from 'react';
import { useAppDispatch, useAppSelector } from '../hooks';
import { fetchGrepData } from '../features/grepSlice';
import { Container, SimpleGrid, Grid, TextInput, Textarea, Center, Text } from '@mantine/core';
import classes from '../styles.module.css';


import CheckIcon from '../svgs/circle-check.svg';
import XIcon from '../svgs/circle-x.svg';
import BlankIcon from '../svgs/whirl.svg';


interface GrepperProps {
    extractedText: string | null;
    shouldReplaceText: boolean;
  }

const Grepper: React.FC<GrepperProps> = ({ extractedText, shouldReplaceText }) => {
    // states for input fields
    const [string, setString] = useState(''); 
    const [regex, setRegex] = useState('');

    // redux states and dispatch
    const { loading, data, error } = useAppSelector((state) => state.grep);
    const dispatch = useAppDispatch();

    // handle form submission
    const handleSubmit = () => {
        dispatch(fetchGrepData({ string, regex }));
    }
    // handle input change for string
    const handleStringChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        const newValue = e.target.value;
        setString(newValue);
        dispatch(fetchGrepData({ string: newValue, regex }));
    }

    // handle input change for regex
    const handleRegexChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        const newValue = e.target.value;
        setRegex(newValue);
        dispatch(fetchGrepData({ string, regex: newValue }));
    }

    let statusIcon;
    if (!string && !regex) {
        statusIcon = <img src={BlankIcon} alt="Blank"  />;
    } else if (data && data.status) {
        statusIcon = <img src={CheckIcon} alt="T"  />;
    } else if (data && !data.status) {
        statusIcon = <img src={XIcon} alt="F"  />;
    }
    else {
        statusIcon = <img src={BlankIcon} alt="Blank"  />;
    }


    useEffect(() => {
        if (shouldReplaceText) {
            if (extractedText != null) setString(extractedText);
            else setString("")
        }
    }, [extractedText, shouldReplaceText]);


    return (
        <div >
            {/* bg="var(--mantine-color-blue-light)" */}
            <Container size="responsive" >
                
                <SimpleGrid cols={2}>

                {/* <Grid>
                    <Grid.Col span={2}>1</Grid.Col>
                    <Grid.Col span={2}>2</Grid.Col> */}
                    <div className={classes.gridColumn}>
                        <Text size="lg" c="violetPanda.2">String</Text>
                        <Textarea
                        classNames={{
                            wrapper: classes.textareaWrapper,
                            // input: `${classes.textareaInput} ${textColorClass}`,
                            input: classes.textareaInput,
                          }}
                        // label="String"
                        value={string}
                        placeholder="aab"
                        c="violetPanda.2"
                        onChange={handleStringChange} 
                        autosize
                        minRows={2}
                        />
                    </div>

                    <div className={classes.gridColumn}>
                    <Text size="lg" c="violetPanda.2">Regex</Text>
                        <Textarea
                        classNames={{
                            input: classes.textareaInput,
                          }}
                        // label="Regex"
                        placeholder="(a)*b"
                        c="violetPanda.1"
                        // style={{ color: textColor }}
                        onChange={handleRegexChange} 
                        autosize
                        minRows={2}
                        />
                    </div>

                </SimpleGrid>
                <Center>
                    <div>
                        {/* <header>Result:</header> */}
                        <Center> {statusIcon} </Center>
                    </div>
                    
                </Center>
                
                {/* </Grid> */}

                {/* <button onClick={handleSubmit}>Submit</button> */}
                
                {/* {loading && <p>Loading...</p>}
                {error && <p>Error: {error}</p>}
                {data && (
                    <div>
                        <p>Status: {data.status.toString()}</p>
                        <p>NFA: {JSON.stringify(data.nfa)}</p>
                        <p>Path: {JSON.stringify(data.path)}</p>
                    </div>
                )} */}
                
                
            
                
            </Container>
            
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