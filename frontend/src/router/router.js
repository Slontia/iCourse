import Index from './components/Index.vue'
import Login from './components/Login.vue'

const routers = [
	{
	path: '/index',
	name: 'index',
	component: Index,
	children: [
		{
			path: '/',
			name: 'login',
			component: Login
		}
	]
	},
	{
		path:'/',
		component: Index,
		children: [
			{
				path: '/',
				component: Login
			}
		]
	}
]
export default routers