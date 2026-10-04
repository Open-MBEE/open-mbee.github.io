package OpenMBEE {
    doc /* How the parts of OpenMBEE fit together.
         * Parts, ports and connectors only (no definitions). */

    part openmbee {
        doc /* Open source community developing a digital engineering suite,
             * with the goal of an open, collaborative community around digital
             * engineering and a focus on open source MBSE and SysML capability. */

        // ---------------------------------------------------------------
        // The digital engineering suite
        // ---------------------------------------------------------------
        part suite {

            part openSysML {
                doc /* Open source SysML modeling suite: tools, apps and runtimes.
                     * SysML language infrastructure that works in harmony
                     * with the rest of OpenMBEE. */
                port languageServices;
                port modelOutput;
                port standardsLink;
                port practiceLink;
            }

            part mms {
                doc /* Model Management System. Services around a graph repository
                     * providing a git-for-graphs experience. Stores integrated models
                     * as graphs and forms digital threads across heterogeneous content. */
                part graphRepository {
                    port graphStore;
                    port versioning;
                }
                part sysmlExtension     { port sysmlAPI; }
                part graphqlExtension   { port graphqlAPI; }
                part oslcExtension      { port oslcAPI; }
                part integrationFramework {
                    doc /* Framework for integrating other services for modeling languages. */
                    port graphIntake;
                    port languageAdapters;
                }

                // external-facing ports of MMS
                port modelAccess;
                port repoAccess;
                port threadIngest;
                port adapterAccess;
                port integrationLink;

                connect graphRepository.graphStore to sysmlExtension.sysmlAPI;
                connect graphRepository.graphStore to graphqlExtension.graphqlAPI;
                connect graphRepository.graphStore to oslcExtension.oslcAPI;
                connect graphRepository.graphStore to integrationFramework.graphIntake;
            }

            part mdk {
                doc /* Model Development Kit. Like an SDK for modeling languages:
                     * tools, integrations and examples for model developers.
                     * Mostly SysML-based today, aimed at model-driven digital engineering. */
                port mmsLink;
                port repoLink;
                port examples;
            }

            part viewEditor {
                doc /* View-based authoring and reporting for integrated modeling
                     * content stored in MMS. Built on ISO 42010 views and viewpoints,
                     * leading to digital twins with introspective qualities. */
                part viewpoints { port viewpointSpec; }
                part views      { port viewContent; }
                port modelAccess;
                port reportOutput;

                connect viewpoints.viewpointSpec to views.viewContent;
            }

            part openContent {
                doc /* Open source models, libraries, graphs, ontologies and analysis,
                     * invited and hosted by OpenMBEE. A growing collection. */
                part models     { port modelSource; }
                part libraries  { port librarySource; }
                part graphs     { port graphSource; }
                part ontologies { port ontologySource; }
                part analysis   { port analysisSource; }
                port contentOut;
                port contributionLink;

                connect models.modelSource         to contentOut;
                connect libraries.librarySource    to contentOut;
                connect graphs.graphSource         to contentOut;
                connect ontologies.ontologySource  to contentOut;
                connect analysis.analysisSource    to contentOut;
            }

            // -----------------------------------------------------------
            // How the suite parts connect
            // -----------------------------------------------------------
            connection openSysMLToMms
                connect openSysML.modelOutput to mms.modelAccess;

            connection viewEditorToMms
                connect viewEditor.modelAccess to mms.modelAccess;

            connection mdkToMms
                connect mdk.mmsLink to mms.modelAccess;

            connection openContentToMms
                connect openContent.contentOut to mms.threadIngest;
        }

        // ---------------------------------------------------------------
        // Heterogeneous modeling content that MMS connects into digital threads
        // ---------------------------------------------------------------
        part threadSources {
            part sysmlModels  { port modelPort; }
            part rdfGraphs    { port graphPort; }
            part ontologies   { port ontologyPort; }

            part futureLanguages {
                doc /* Possible future modeling languages. */
                part modelica { port modelPort; }
                part simulink { port modelPort; }
                part others   { port modelPort; }
            }

            port threadOut;
            port futureOut;

            connect sysmlModels.modelPort    to threadOut;
            connect rdfGraphs.graphPort      to threadOut;
            connect ontologies.ontologyPort  to threadOut;
            connect futureLanguages.modelica.modelPort to futureOut;
            connect futureLanguages.simulink.modelPort to futureOut;
            connect futureLanguages.others.modelPort   to futureOut;
        }

        connection digitalThread
            connect threadSources.threadOut to suite.mms.threadIngest;

        connection futureLanguageIntegration
            connect threadSources.futureOut to suite.mms.adapterAccess;

        // ---------------------------------------------------------------
        // Existing vendors, standards bodies and communities
        // ---------------------------------------------------------------
        part collaborators {
            doc /* OpenMBEE seeks to collaborate with existing vendors, standards
                 * and communities, primarily OMG and INCOSE, and to be the open
                 * source leg of these entities. */
            part omg {
                doc /* Object Management Group: SysML and related standards. */
                port standardsLink;
            }
            part incose {
                doc /* International Council on Systems Engineering. */
                port practiceLink;
            }
            part vendors {
                port integrationLink;
            }
            part otherStandardsAndCommunities {
                port contributionLink;
            }
        }

        connection omgToOpenSysML
            connect collaborators.omg.standardsLink to suite.openSysML.standardsLink;

        connection incoseToOpenSysML
            connect collaborators.incose.practiceLink to suite.openSysML.practiceLink;

        connection vendorsToMms
            connect collaborators.vendors.integrationLink to suite.mms.integrationLink;

        connection communitiesToOpenContent
            connect collaborators.otherStandardsAndCommunities.contributionLink
                to suite.openContent.contributionLink;

        // ---------------------------------------------------------------
        // Community that supports development of everything above
        // ---------------------------------------------------------------
        part community {
            doc /* Community-supported development. */
            part chat          { port channel; }
            part emailGroups   { port channel; }
            part github {
                doc /* Source repositories for the suite. */
                port repos;
                port channel;
            }
            part buildServices { port pipeline; }
            part webHosting    { port site; }
            part socialAndWebMedia { port presence; }

            port developmentSupport;

            connect chat.channel          to developmentSupport;
            connect emailGroups.channel   to developmentSupport;
            connect github.channel        to developmentSupport;
            connect buildServices.pipeline to github.repos;
            connect webHosting.site       to socialAndWebMedia.presence;
        }

        connection communityToSuite
            connect community.developmentSupport to suite.mms.repoAccess;

        connection mdkToGithub
            connect suite.mdk.repoLink to community.github.repos;

        connection openSysMLToGithub
            connect suite.openSysML.languageServices to community.github.repos;
    }
}
