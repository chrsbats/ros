# ROS-lite


An approximate, ROS-inspired utility to estimate the mean and standard deviation of a left-censored, approximately normal dataset.

> ⚠️ This is not a full Regression on Order Statistics (ROS) implementation. It does **not** perform imputation or regression on censored values. It uses uncensored data and assumed plotting positions to estimate normal parameters via least-squares fitting.
> ⚠️ Archived: This was a one-off tool written in 2014 for a specific project. Not maintained. 

## Why use this?

- You have sensor or environmental data with left-censoring (e.g., detection limits).
- You need a quick estimate of the underlying distribution without full ROS machinery.
- You want a pure-Python, dependency-light approach.

## What it does

- Takes uncensored values and the count of non-detects.
- Computes plotting positions assuming left-censoring.
- Optimizes a normal distribution (mean/std) to match those quantiles via least-squares.

## What it doesn't do

- No imputation for censored values
- No generalized ROS support (e.g., Kaplan-Meier, multi-bound censoring)
