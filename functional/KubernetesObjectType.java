package com.tidalsoft.service.kubernetes.webclient.client.global;

/**
 * @author Eugene Markovich
 * on 18/01/2021
 */
public enum KubernetesObjectType {

    POD("Pod") {
        @Override
        public String getTagName() {
            return "pod";
        }
    },
    REPLICA_SET("ReplicaSet") {
        @Override
        public String getTagName() {
            return "replicaSet";
        }
    },
    DEPLOYMENT("Deployment") {
        @Override
        public String getTagName() {
            return "deployment";
        }
    },
    SERVICE("Service") {
        @Override
        public String getTagName() {
            return "service";
        }
    },
    CONFIG_MAP("ConfigMap") {
        @Override
        public String getTagName() {
            return "configMap";
        }
    },
    PERSISTENT_VOLUME_CLAIM("PersistentVolumeClaim") {
        @Override
        public String getTagName() {
            return "persistentVolumeClaim";
        }
    };

    private final String name;

    KubernetesObjectType(final String name) {
        this.name = name;
    }

    public abstract String getTagName();

    public String getName() {
        return name;
    }
}
