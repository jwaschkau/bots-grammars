#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99},
    {ID: 'CUX', MIN: 0, MAX: 99},
    {ID: 'FTX', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CAV', MIN: 0, MAX: 1},
    ]},
    {ID: 'SEQ', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'CPT', MIN: 0, MAX: 4},
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'IND', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'RFF', MIN: 1, MAX: 1},
            {ID: 'FTX', MIN: 1, MAX: 1},
            {ID: 'LIN', MIN: 1, MAX: 999, LEVEL: [
                {ID: 'CPT', MIN: 0, MAX: 4},
                {ID: 'RJL', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 1},
                {ID: 'PAI', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'TAX', MIN: 0, MAX: 9},
                {ID: 'FII', MIN: 0, MAX: 1},
                {ID: 'CUX', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 1, MAX: 9},
                {ID: 'CCI', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'CAV', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'QTY', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 1, MAX: 9},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'QTY', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 1, MAX: 9},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
