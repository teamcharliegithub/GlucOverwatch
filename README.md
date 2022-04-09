# GlucOverwatch

GlucOverwatch is an application that helps people with diabetes monitor their blood sugar levels.

## Motivation

In the US alone, there are nearly 2 million people with Type 1 diabetes. This chronic condition causes the pancreas to produce little or no insulin. Therefore, to ensure the patients' safety, the health workers must keep track of their blood sugar levels. In case the level is too low, the caregivers must take immediate action to seek help.

The biomedical companies have already developed devices to track the blood sugar level every few minutes. However, there still lacks a service to notify the health workers of any urgent situation. Hence, if a patient's blood sugar suddenly drops significantly, there is no viable way to inform the caregivers.

## Solution

We want to solve this problem. Thus, we build GlucOverwatch, a computer program that monitors the data output from the glucose monitor device. 

GlucOverwatch includes a Python program, which sends API requests every 6 minutes to the glucose monitor hardware. Thus, it can get up-to-date data about the user's glucose level. If there are any significant changes, the app will send notifications to the patients and their caregivers, so they can stay informed of the situation.
