#### Models and Cookbooks

OpenMBEE has several open source modeling projects built within the OpenMBEE Software

<br>

#### Thirty Meter Telescope SysML Model

TMT is currently being developed by the [TMT Observatory Corporation](http://www.tmt.org){:target="_blank"}. The TMT SysML model provides an industrial scale application of OpenMBEE and system-level behavior simulation. The main objective for the TMT related analysis is to provide state-dependent power roll-ups for different operational scenarios and demonstrate that requirements are satisfied by the design as well as mass roll-ups and duration analysis of the operational use cases. The model is built with an approach to model-based systems analysis with SysML that is both rigorous and automated. The approach’s rigor is established with a modeling method that is an extension of [INCOSE](http://www.incose.org){:target="_blank"}’s Object Oriented Systems Engineering Method (OOSEM).

The SysML model is accessible on twc.openmbee.org. The engineering document created from the model are accessible on [mms.openmbee.org](https://mms.openmbee.org/alfresco/mmsapp/mms.html#/projects/PROJECT-d94630c2-576c-4edd-a8cd-ae3ecd25d16c/master){:target="_blank"}

<br>

#### OpenMBEE Architectural Model

The OpenMBEE group is developing an architectural model to link user needs, functionality, and technical design of the integrated environment. The architectural model describes a set of modeling styles and the various questions that the environment is intended to help users answer. The model also catalogs major functionality and APIs to access.

The model is used to generate a document to describe the architecture and another to describe major components.

The OpenMBEE Architectural Model model can be downloaded from GitHub in the arch_model repository. The engineering documents created from the model are accessible on [mms.openmbee.org](https://mms.openmbee.org/alfresco/mmsapp/mms.html#/projects/PROJECT-f2f8bbae-a00b-4e02-bbe8-6d84fa3c219e/master){:target="_blank"}

<br>

#### Cookbooks

Engineering cookbooks are a compendium for the engineer which captures best practices, lessons learned, and provides guidance on how to use languages and tools to achieve a certain engineering task, such as “How-to Verify Requirements”.
        
The OpenSE Cookbook is an open-sourced collection of patterns, procedures, and best practices targeted for systems engineers who seek guidance on applying model-based and executable systems engineering using SysML. Its content has emerged from the system level modeling effort on the European Framework Program 6 (FP6) and the Thirty Meter Telescope.

Application of the OpenSE Cookbook practices enables consistent delivery of engineered products using a well-defined modeling approach called the Executable Systems Engineering Method ([ESEM](https://github.com/Open-MBEE/TMT-SysML-Model/blob/master/Presentations/SPIE_2016_Creating_Systems_Engineering_Products_With_Executable_Models_In_A_Model-Based_Engineering_Environment.docx){:target="_blank"}), which is a refinement of the Object Oriented Systems Engineering Method (OOSEM).

ESEM introduces the next phase of system modeling emphasizing executable models to enhance understanding, precision, and verification of requirements.

The OpenSE Cookbook provides a consistent, comprehensive, detailed, and background-agnostic set of operational procedures to guide practitioners through MBSE. Unlike existing SysML literature whose goal is to provide the foundations of descriptive modeling to newcomers and bring forward the arguments in favor of MBSE, the OpenSE Cookbook represents an implementation of what such literature often refers to as best practices or organization-specific procedures. It provides goal oriented guidance for systems engineers explained by a set of combinable patterns. Systems engineering workflows drive each of the pattern definitions, such as how to verify requirements, roll-up technical resources, and analysis.

The OpenSE Cookbook demonstrates how to build and analyze system models using OpenMBEE as applied to educational examples as well as actual usages in the TMT production model.

The overall goal of the OpenSE Cookbook in conjunction with OpenMBEE is to commoditize the Executable Systems Engineering Method, i.e. remove the cost and barriers to entry that allows for expanded innovation and broader operations driven by increased user access and decreased costs, in order to foster the broadest adoption.

The OpenSE Cookbook is available
   * [Online OpenSE Cookbook](https://mms.openmbee.org/alfresco/mmsapp/mms.html#/projects/PROJECT-ID_2_2_17_7_33_25_AM_3ccfaf88_159fe0d7ba9__7d4e_cae_tw_jpl_nasa_gov_127_0_0_1/master/document/_18_5_2_e64033a_1513276256458_934885_22190){:target="_blank"}
   * [Offline OpenSE Cookbook](https://github.com/Open-MBEE/OpenSE-Cookbook){:target="_blank"}

This [OpenSE Cookbook paper](https://github.com/Open-MBEE/TMT-SysML-Model/blob/master/Presentations/OpenSE-Cookbook-Paper-SPIE-2018.pdf){:target="_blank"} provides an in-depth overview.

The orginal version of the cookbook can be found [here](http://mbse.gfse.de/documents/faq.html){:target="_blank"}. It was created by the [INCOSE Telescope Modeling Challenge Team](http://omgwiki.org/MBSE/doku.php?id=mbse:telescope){:target="_blank}

<br>

#### Model Libraries

The OpenSE Cookbook is accompanied by the [OpenSE model library](https://mms.openmbee.org/alfresco/mmsapp/mms.html#/projects/PROJECT-6e50f60a-ee13-4ee7-bd3a-e39338890c2d/master/document/_18_0_6_bec02f9_1498838354230_843679_41313){:target="_blank"} that provides model templates (e.g. to support ESEM), structural elements (e.g. for organizational charts), and behavioral elements to facilitate the authoring and analysis of models following the described patterns.

A library of platform independent [re-usable behavioral models](https://github.com/Open-MBEE/Comodo/tree/master/Models/Devices){:target="_blank"} for different devices, such as lamps and motors, has been developed by the European Southern Observatory ([ESO](https://www.eso.org){:target="_blank"}) to build Telescope and Instrument control and supervisor applications for different [software platforms](https://github.com/Open-MBEE/Comodo/blob/master/docs/OpenSourceBehaviouralModels.pptx){:target="_blank"}.
