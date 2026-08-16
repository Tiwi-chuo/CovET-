CovET : Covert Eye-Tracking for Peripheral Brand Recognition

Overview

CovET (Covert Eye-Tracking) is an experimental framework designed to investigate covert brand recognition in peripheral vision by combining eye-tracking data with a Go/No-Go behavioral task.
Traditional eye-tracking analysis primarily evaluates visual attention based on overt gaze behavior, such as fixations on a stimulus or Area of Interest (AOI). However, visual information can also be processed without direct fixation.
CovET was developed to examine this phenomenon by identifying whether participants can correctly recognize a target brand even when their gaze does not directly fall on the brand logo.

In this framework:
•	Eye tracking determines where the participant is looking.
•	Visual-angle-based regions determine whether the target falls within or outside central vision.
•	Go/No-Go responses indicate whether the participant correctly recognizes the target.
•	These signals are combined to identify trials in which correct recognition occurs without direct fixation on the target.
The framework was developed to investigate whether highly familiar brands can be recognized through peripheral vision before deliberate visual exploration.

Concept
CovET distinguishes between overt visual attention and covert recognition.
Overt Attention
The participant directly looks at the target stimulus.
        Gaze
          ↓
      [ BRAND ]
The brand falls within the participant's central visual field.

Covert Recognition

The participant's gaze is directed elsewhere, but the target brand remains available in peripheral vision.
Gaze
 ↓

 ●  ----------------------  [ BRAND ]
          peripheral
            vision
If the participant correctly performs the Go/No-Go task despite not directly fixating on the target, the trial may indicate covert recognition.

Experimental Paradigm
CovET combines an eye-tracking experiment with a Go/No-Go task.
Participants are instructed to:
Press the space bar when the displayed logo is NOT the target brand, and do not press the space bar when the target brand appears.
Therefore:
Non-target brand
      ↓
Press SPACE
      ↓
GO response
while:
Target brand
      ↓
Do NOT press SPACE
      ↓
NO-GO response
Correct No-Go responses provide behavioral evidence that the participant recognized the target brand.
Eye-tracking data are then used to determine where the participant was looking when this recognition occurred.

CovET Logic
The basic analysis combines two sources of information:
                 Visual Stimulus
                       │
                       ▼
                Eye-Tracking Data
                       │
                       ▼
              Fixation Detection
                       │
                       ▼
          Visual-Angle Classification
             │                    │
             ▼                    ▼
          Foveola               Fovea
             │                    │
             └─────────┬──────────┘
                       │
                       ▼
              Gaze–Target Relation
                       │
                       │
         Go/No-Go Behavioral Response
                       │
                       ▼
             Recognition Accuracy
                       │
                       ▼
          Eye Tracking × Behavior
                       │
                       ▼
             Covert Recognition
             
The key question is:
Was the participant able to correctly recognize the target brand even though the target was not directly fixated?

Visual Field Classification
CovET evaluates gaze relative to the target using visual-angle-based regions around each fixation.
Two central visual regions are considered:
Foveola
The foveola represents the most central region of vision and provides the highest visual acuity.
Fovea
The fovea represents a broader region of central vision surrounding the fixation point.
Conceptually:

              FOVEA
       ┌─────────────────┐
       │                 │
       │     FOVEOLA     │
       │      ┌───┐      │
       │      │ ● │      │
       │      └───┘      │
       │                 │
       └─────────────────┘

                ●
            fixation
            
This approach makes it possible to evaluate whether recognition occurs when a brand is located inside or outside different regions of central vision.

Fixation Detection
Raw eye-tracking data are processed to identify fixations.
Fixation detection is performed using the I2MC (Identification by Two-Means Clustering) algorithm:
Hessels, R. S., Niehorster, D. C., Kemner, C., & Hooge, I. T. C. (2017). Noise-robust fixation detection in eye movement data: Identification by two-means clustering (I2MC). Behavior Research Methods, 49, 1802–1823.
For the present implementation, the I2MC processing procedure was adapted for the experimental eye-tracking data.

Experimental Setup
The framework was developed using eye-tracking data collected with:
Eye Tracker:
Tobii Pro Spectrum

Sampling Rate:
1200 Hz

Stimulus Resolution:
1920 × 1080 pixels
The experiment integrates eye-tracking recording with the Go/No-Go task so that gaze behavior and behavioral responses can be evaluated on a trial-by-trial basis.


Analysis Workflow
The overall CovET processing pipeline can be summarized as:
Raw Eye-Tracking Data
        │
        ▼
Fixation Detection
(I2MC)
        │
        ▼
Fixation Coordinates
        │
        ▼
Visual Angle Calculation
        │
        ▼
Foveola / Fovea Classification
        │
        ▼
Target Position Relative to Gaze
        │
        ├───────────────┐
        │               │
        ▼               ▼
 Direct Fixation     Outside Central
                       Vision
        │               │
        └───────┬───────┘
                │
                ▼
        Go/No-Go Response
                │
                ▼
       Recognition Accuracy
                │
                ▼
      Covert Recognition
        Classification



Correct Covert Ratio (CCR)
CovET can be used to calculate the Correct Covert Ratio (CCR).
CCR represents the proportion of trials in which the target is correctly recognized without direct visual fixation on the target.
Conceptually:
              Correct covert recognition trials
CCR = ------------------------------------------------
             Eligible target recognition trials
A higher CCR indicates that the stimulus can be correctly recognized more frequently without direct fixation.
In brand research, this metric can be used to investigate whether highly familiar or visually strong brands are more likely to be recognized through peripheral vision.

Application to Brand Recognition
The original CovET experiment was developed to investigate brand recognition under peripheral viewing conditions.
The framework compares brands with different levels of familiarity to examine whether prior brand knowledge facilitates recognition outside direct fixation.
The underlying hypothesis is that highly familiar brands may activate stored brand representations rapidly enough to support recognition before deliberate visual exploration occurs.
Therefore, CovET provides a way to investigate a stage of visual brand processing that may not be captured by conventional fixation-based metrics alone.


Repository Structure
The repository contains scripts for experimental control, eye-tracking processing, fixation detection, visualization, and covert-recognition analysis.
A general structure is:
CovET/
│
├── experiment/
│   └── experimental task scripts
│
├── eye_tracking/
│   └── eye-tracker connection and recording
│
├── fixation_detection/
│   └── I2MC-based fixation processing
│
├── analysis/
│   └── covert recognition analysis
│
├── visualization/
│   └── gaze trajectory visualization
│
└── README.md
The exact folder structure may differ depending on the version of the repository.
Visualization
Gaze trajectories and fixation locations can be visualized using Python-based processing.
The visualization procedure allows researchers to inspect:
•	fixation locations,
•	gaze trajectories,
•	target locations,
•	foveolar regions,
•	foveal regions, and
•	potential covert-recognition trials.
These visualizations are primarily intended for interpretation and quality control of the gaze classification procedure.


Related Tools
I2MC
Fixation detection is based on the I2MC algorithm developed by Hessels et al. (2017).
Repository:
https://github.com/royhessels/I2MC
Titta
Parts of the eye-tracker connection and experimental implementation were adapted from or developed with reference to Titta, a Python toolbox for controlling Tobii eye trackers.
Appropriate acknowledgment and references to the original Titta implementation should therefore be retained when using the corresponding components of this repository.

Important Notes
CovET should not be interpreted as direct evidence of unconscious visual processing.
Instead, the framework operationalizes covert recognition as correct behavioral recognition occurring when gaze-based analysis indicates that the target was not directly fixated within the specified central visual region.
The interpretation therefore depends on:
•	eye-tracking accuracy,
•	fixation detection,
•	visual-angle thresholds,
•	behavioral-response accuracy, and
•	experimental design.
Researchers should select visual-angle parameters appropriate for their experimental setup and research question.


Research Use
CovET was developed for research on:
•	visual attention,
•	peripheral vision,
•	covert attention,
•	brand recognition,
•	consumer neuroscience,
•	neuromarketing, and
•	eye-tracking methodology.

Although initially developed for brand-logo recognition, the framework may potentially be adapted to other visual-recognition paradigms where researchers want to examine recognition without direct fixation.
Citation
If you use CovET in academic research, please cite the associated publication.
Citation information will be added after publication.

Authors
Pratiwi Christin Harnita, Otoha Yamanaka, Koki Amano, Kodai Machida, Dan Ippeita
Chuo University, Japan
CovET was developed as part of research investigating covert visual attention and brand recognition using eye tracking and behavioral responses.
License
License information will be added to this repository.
Contact
For questions regarding the CovET framework, experimental paradigm, or research collaboration, please contact the corresponding author.

<img width="468" height="651" alt="image" src="https://github.com/user-attachments/assets/dd3ad6bc-2ec9-4f76-8bb7-caf477709962" />
