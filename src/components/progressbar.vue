<template>
    <div class="progressbar">
        <div class="progressbar-icon">
            <svg v-if="icon === 'req'" xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="48px" viewBox="0 0 24 24" width="24px" fill="#11CCEE"><rect fill="none" height="24" width="24"/><path d="M15,5l-1.41,1.41L18.17,11H2V13h16.17l-4.59,4.59L15,19l7-7L15,5z"/></svg>
            <svg v-if="icon === 'res'" xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" viewBox="0 0 24 24" width="24px" fill="#FF2400"><rect fill="none" height="24" width="24"/><path d="M9,19l1.41-1.41L5.83,13H22V11H5.83l4.59-4.59L9,5l-7,7L9,19z"/></svg>
            <svg v-if="icon === 'wait'" xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" viewBox="0 0 24 24" width="24px" fill="#bad1ce"><g><rect fill="none" height="24" width="24"/></g><g><path d="M12,2C6.48,2,2,6.48,2,12c0,5.52,4.48,10,10,10s10-4.48,10-10C22,6.48,17.52,2,12,2z M7,13.5c-0.83,0-1.5-0.67-1.5-1.5 c0-0.83,0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5C8.5,12.83,7.83,13.5,7,13.5z M12,13.5c-0.83,0-1.5-0.67-1.5-1.5 c0-0.83,0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5C13.5,12.83,12.83,13.5,12,13.5z M17,13.5c-0.83,0-1.5-0.67-1.5-1.5 c0-0.83,0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5C18.5,12.83,17.83,13.5,17,13.5z"/></g></svg>
        </div>
        <div class="progressbar-messages">
            <h2 id="progressbar-messages">Sending request to Flask...</h2>
        </div>
        <div class="progressbar-line">

        </div>
    </div>
</template>

<script>
    export default {
        props: {
            icon: {
                type: String,
                required: true
            }
            },
        methods: {
            setIcon(type) {
                return type;
            }
        }
    }
</script>

<style lang="scss" scoped>

@keyframes loading {
    0% {
        opacity: 0%;
    }
    50% {
        opacity: 100%;
    }
    100% {
        opacity: 0%;
    }
}

.progressbar {
    position: fixed;
    width: 100%;
    height: 50px;
    bottom: 0;
    left: 0;
    right: 0;
    cursor: default;
    display: flex;
    flex-direction: row;
    background: rgba(0,0,0,0.7);
}

.progressbar-icon {
    width: 10%;
    display: flex;
    align-items: center;
    justify-content: center;
    svg {
        animation-name: loading;
        animation-duration: 1.5s;
        animation-iteration-count: infinite;
    }
}

.progressbar-messages {
    width: 90%;
    color: white;
    font-size: 10px;
    text-justify: center;
}

</style>